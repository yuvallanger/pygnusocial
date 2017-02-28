"""
gnusocial.utils
~~~~~~~~~~~~~~~

Module with various utility functions and exception classes.
"""
import re
from typing import Callable
from functools import partial
import requests
from dtd import docstring
from .docs import _SERVER_URL_DOC, _CONFIG_DICT, _USERNAME_DOC, _PASSWORD_DOC

DOMAIN_REGEX = re.compile(r"http(s|)://(www\.|)(.+?)(/.*|)$")


class GNUSocialAPIError(Exception):
    """Exception class for API errors.

:param str error_message: API error message.
    """
    def __init__(self, error_message: str) -> None:
        self.error_message = error_message
        super().__init__(Exception)

    def __repr__(self) -> str:
        return 'GNUSocialAPIError(%r)' % self.error_message

    def __str__(self) -> str:
        return 'API error: %s' % self.error_message


@docstring(server_url=_SERVER_URL_DOC)
class ServerURLError(Exception):
    """Exception class for errors in server URL.

:param str server_url: {server_url}
    """
    def __init__(self, server_url: str) -> None:
        self.server_url = server_url
        super().__init__(Exception)

    def __repr__(self) -> str:
        return 'ServerURLError(%r)' % self.server_url

    def __str__(self) -> str:
        return 'Invalid server URL %s' % self.server_url


@docstring(server_url=_SERVER_URL_DOC,
           username=_USERNAME_DOC,
           password=_PASSWORD_DOC)
class AuthenticationError(Exception):
    """Exception class for authentication errors.

:param str server_url: {server_url}
:param str username: {username}
:param str password: {password}
    """
    def __init__(self, server_url: str, username: str, password: str) -> None:
        self.server_url = server_url
        self.username = username
        self.password = password
        super().__init__(self)

    def __repr__(self) -> str:
        return 'AuthenticationError(%r, %r, %r)' % (self.server_url,
                                                    self.username,
                                                    self.password)

    def __str__(self) -> str:
        return 'Invalid credentials for (%s, %s)' % (self.username,
                                                     self.server_url)


def _check_auth_error(response: requests.models.Response,
                      server_url: str,
                      username: str,
                      password: str) -> None:
    if response.status_code == 401:
        raise AuthenticationError(server_url, username, password)


def _api_path(server_url: str) -> str:
    _validate_server_url(server_url)
    if server_url[-1] != '/':
        server_url += '/'
    return server_url + 'api/'


def _validate_server_url(server_url: str) -> None:
    if not DOMAIN_REGEX.match(server_url):
        raise ServerURLError(server_url)


def _check_connection(server_url: str) -> None:
    response = _get_request(server_url, 'help/test').json()
    if response != 'ok':
        raise requests.ConnectionError(server_url)


def _resource_url(server_url: str,
                  resource_path: str,
                  extension: str='.json') -> str:
    return _api_path(server_url) + resource_path + extension


def _request(request_func: Callable,
             server_url: str,
             resource_path: str,
             **kwargs) -> requests.models.Response:
    extension = kwargs.get('extension', '.json')
    req = partial(request_func,
                  url=_resource_url(server_url, resource_path, extension),
                  data=kwargs.get('data'),
                  files=kwargs.get('media'),
                  params=kwargs.get('params'))
    response = None
    username = kwargs.get('username')
    oauth = kwargs.get('oauth')
    if username and oauth:
        raise ValueError("You can't use HTTP Basic Auth and OAuth at the same" +
                        "time.")
    if username:
        password = kwargs.get('password')
        response = req(auth=(username, password))
        _check_auth_error(response, server_url, username, password)
    elif oauth:
        response = req(auth=oauth)
    else:
        response = req()
    if extension == '.json':
        response_json = response.json()
        if 'error' in response_json:
            raise GNUSocialAPIError(response_json['error'])
    return response


def _get_request(server_url: str,
                 resource_path: str,
                 **kwargs) -> requests.models.Response:
    return _request(request_func=requests.get,
                    server_url=server_url,
                    resource_path=resource_path,
                    **kwargs)


def _post_request(server_url: str,
                  resource_path: str,
                  **kwargs) -> requests.models.Response:
    return _request(request_func=requests.post,
                    server_url=server_url,
                    resource_path=resource_path,
                    **kwargs)


@docstring(server_url=_SERVER_URL_DOC, config_dict=_CONFIG_DICT)
def config(server_url: str) -> dict:
    """Returns server configuration.

:param str server_url: {server_url}
:rtype: dict
:return: dict with following structure:

::

    {config_dict}

    """
    return _get_request(server_url, 'statusnet/config').json()


def _check_user_target(username: str='', use_username=False, **kwargs) -> None:
    both_targets = 'user_id' in kwargs and 'screen_name' in kwargs
    no_targets = 'user_id' not in kwargs and 'screen_name' not in kwargs
    if both_targets:
        raise ValueError(
            "You must either specify the user_id or screen_name."
        )
    if no_targets and not use_username:
        raise ValueError(
            "You must either specify the user_id or screen_name."
        )
    elif no_targets and use_username and not username:
        raise ValueError(
            "You must either specify the user_id or screen_name or " +
            "username."
        )


def _check_id_and_nickname(**kwargs) -> None:
    has_group_id = 'id' in kwargs
    has_group_name = 'nickname' in kwargs
    if has_group_id == has_group_name:
        raise ValueError(
            "You must either specify the id or nickname."
        )


def _check_group_id_and_name(**kwargs) -> None:
    has_group_id = 'group_id' in kwargs
    has_group_name = 'group_name' in kwargs
    if has_group_id == has_group_name:
        raise ValueError(
            "You must either specify the group_id or group_name."
        )
