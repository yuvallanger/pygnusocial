"""
gnusocial.utils
~~~~~~~~~~~~~~~

Module with various utility functions and exception classes.
"""
import re
from typing import Callable
from functools import partial
import requests
from requests.auth import HTTPBasicAuth

DOMAIN_REGEX = re.compile(r"http(s|)://(www\.|)(.+?)(/.*|)$")


class ServerURLError(Exception):
    """Exception class for errors in server URL.

    :param server_url: URL of the server
    """
    def __init__(self, server_url: str) -> None:
        self.server_url = server_url
        super().__init__(Exception)

    def __repr__(self) -> str:
        return 'ServerURLError(%r)' % self.server_url

    def __str__(self) -> str:
        return 'Invalid server URL %s' % self.server_url


class AuthenticationError(Exception):
    """Exception class for authentication errors.

    :param server_url: URL of the server
    :param username: name of the authenticating user
    :param password: password of the authenticating user
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
        return 'Invalid credentials %s:%s for %s' % (self.username,
                                                     self.password,
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
             username: str='',
             password: str='',
             **kwargs) -> requests.models.Response:
    extension = kwargs.get('extension') or '.json'
    req = partial(request_func,
                  url=_resource_url(server_url, resource_path, extension),
                  data=kwargs.get('data'),
                  files=kwargs.get('media'),
                  params=kwargs.get('params'))
    response = None
    if username:
        response = req(auth=HTTPBasicAuth(username, password))
        _check_auth_error(response, server_url, username, password)
    else:
        response = req()
    response.raise_for_status()
    return response


def _get_request(server_url: str,
                 resource_path: str,
                 username: str='',
                 password: str='',
                 **kwargs) -> requests.models.Response:
    return _request(request_func=requests.get,
                    server_url=server_url,
                    resource_path=resource_path,
                    username=username,
                    password=password,
                    **kwargs)


def _post_request(server_url: str,
                  resource_path: str,
                  username: str='',
                  password: str='',
                  **kwargs) -> requests.models.Response:
    return _request(request_func=requests.post,
                    server_url=server_url,
                    resource_path=resource_path,
                    username=username,
                    password=password,
                    **kwargs)


def config(server_url: str) -> dict:
    """Returns server configuration.

    :param server_url: URL of the server
    :return: dict with following structure:
        attachments
            file_quota - maximum size of attachment in bytes
            uploads - True if users are allowed to upload files
        group
            desclimit
        integration
            source
        license
            image
            owner
            title
            type
            url
        nickname
            featured
        notice
            contentlimit
        profile
            biolimit
        site
            broughtby
            broughtbyurl
            closed
            email
            fancy
            inviteonly
            language
            logo
            name
            path
            private
            server
            ssl
            sslserver
            textlimit
            theme
            timezone
        throttle
            count
            enabled
            timespan
        url
            maxnoticelength
            maxurllength
        xmpp
            enabled
            port
            server
            user
    """
    return _get_request(server_url, 'statusnet/config').json()


def _check_user_target(username: str='', **kwargs) -> None:
    both_targets = 'user_id' in kwargs and 'screen_name' in kwargs
    no_targets = 'user_id' not in kwargs and 'screen_name' not in kwargs
    if both_targets:
        raise Exception(
            "You must either specify the user_id or screen_name."
        )
    if no_targets and not username:
        raise Exception(
            "You must either specify the user_id or screen_name or " +
            "username."
        )


def _check_id_and_nickname(**kwargs) -> None:
    both_targets = 'id' in kwargs and 'nickname' in kwargs
    if both_targets:
        raise Exception(
            "You must either specify the id or nickname."
        )


def _check_group_id_and_name(**kwargs):
    has_group_id = 'group_id' in kwargs
    has_group_name = 'group_name' in kwargs
    if has_group_id == has_group_name:
        raise Exception(
            "You must either specify the group_id or group_name."
        )
