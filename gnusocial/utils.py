import re
from typing import Tuple
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


def _check_auth_error(response: requests.models.Response,
                      server_url: str,
                      username: str,
                      password: str) -> None:
    if response.status_code == 401:
        raise AuthenticationError(server_url, username, password)


def _api_path(server_url: str) -> str:
    if server_url[-1] != '/':
        server_url += '/'
    return server_url + 'api/'


def _validate_server_url(server_url: str) -> None:
    if not DOMAIN_REGEX.match(server_url):
        raise ServerURLError(server_url)


def _check_connection(server_url: str) -> None:
    _validate_server_url(server_url)
    response = _get_request(server_url, 'help/test', extension='.json')
    if response != 'ok':
        raise requests.ConnectionError(server_url)


def _verify_credentials(server_url: str,
                        username: str,
                        password: str) -> None:
    _get_request(
        server_url=server_url,
        resource_path='account/verify_credentials',
        username=username,
        password=password,
        extension='.json'
    )


def _resource_url(server_url: str,
                  resource_path: str,
                  extension: str='.as') -> str:
    return _api_path(server_url) + resource_path + extension


def _get_request(server_url: str,
                 resource_path: str,
                 username: str='',
                 password: str='',
                 **kwargs) -> dict:
    get = partial(requests.get,
                  _resource_url(server_url, resource_path, **kwargs))
    if username:
        response = get(auth=HTTPBasicAuth(username, password))
        _check_auth_error(response, server_url, username, password)
        return response.json()
    else:
        return get().json()


def _post_request(server_url: str,
                  resource_path: str,
                  username: str,
                  password: str,
                  data: dict) -> dict:
    response = requests.post(
        _resource_url(server_url, resource_path, '.json'),
        data=data,
        auth=HTTPBasicAuth(username, password)
    )
    _check_auth_error(response, server_url, username, password)
    return response.json()


def statusnet_config(server_url: str) -> dict:
    return _get_request(server_url, 'statusnet/config')


def login(server_url: str, username: str, password: str) -> None:
    _check_connection(server_url)
    _verify_credentials(server_url, username, password)
