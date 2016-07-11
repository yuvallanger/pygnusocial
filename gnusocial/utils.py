import re
from typing import Tuple, Callable
from functools import partial
import requests
from requests.auth import HTTPBasicAuth

DOMAIN_REGEX = re.compile(r"http(s|)://(www\.|)(.+?)(/.*|)$")


class ServerURLError(Exception):
    def __init__(self, server_url: str) -> None:
        self.server_url = server_url
        super().__init__(Exception)

    def __repr__(self) -> str:
        return 'ServerURLError(%r)' % self.server_url

    def __str__(self) -> str:
        return 'Invalid server URL %s' % self.server_url


class AuthenticationError(Exception):
    def __init__(self, server_url: str, username: str, password: str) -> None:
        self.server_url = server_url
        self.username = username
        self.password = password
        super().__init__(self)

    @property
    def credentials(self) -> Tuple[str, str]:
        return (self.username, self.password)

    def __repr__(self) -> str:
        return 'AuthenticationError(%r, %r, %r)' % (self.server_url,
                                                    self.username,
                                                    self.password)

    def __str__(self) -> str:
        return 'Invalid credentials %s:%s for %s' % (self.username,
                                                     self.password,
                                                     self.server_url)


class InternalServerError(Exception):
    def __init__(self, server_url: str) -> None:
        self.server_url = server_url
        super().__init__(self)

    def __repr__(self) -> str:
        return 'InternalServerError(%r)' % self.server_url

    def __str__(self) -> str:
        return '%s has encountered an internal error' % self.server_url


def _check_internal_error(response: requests.models.Response,
                          server_url: str) -> None:
    if response.status_code == 500:
        raise InternalServerError(server_url)


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
    response = _get_request(server_url, 'help/test')
    if response != 'ok':
        raise requests.ConnectionError(server_url)


def _verify_credentials(server_url: str,
                        username: str,
                        password: str) -> None:
    _get_request(
        server_url=server_url,
        resource_path='account/verify_credentials',
        username=username,
        password=password
    )


def _resource_url(server_url: str,
                  resource_path: str,
                  extension: str='.json') -> str:
    return _api_path(server_url) + resource_path + extension


def _request(request_func: Callable,
             server_url: str,
             resource_path: str,
             username: str='',
             password: str='',
             extension: str='.json',
             data: dict=None):
    req = partial(request_func,
                  _resource_url(server_url, resource_path, extension),
                  data=None)
    response = None
    if username:
        response = req(auth=HTTPBasicAuth(username, password))
        _check_auth_error(response, server_url, username, password)
    else:
        response = req()
    _check_internal_error(response, server_url)
    return response.json()


def _get_request(server_url: str,
                 resource_path: str,
                 username: str='',
                 password: str='',
                 **kwargs):
    return _request(requests.get,
                    server_url,
                    resource_path,
                    username,
                    password,
                    **kwargs)


def _post_request(server_url: str,
                  resource_path: str,
                  username: str='',
                  password: str='',
                  data: dict=None):
    return _request(requests.post,
                    server_url,
                    resource_path,
                    username,
                    password,
                    data=data)


def config(server_url: str) -> dict:
    return _get_request(server_url, 'statusnet/config')


def login(server_url: str, username: str, password: str) -> None:
    _check_connection(server_url)
    _verify_credentials(server_url, username, password)
