import re
from typing import Tuple
import requests
from requests.auth import HTTPBasicAuth

DOMAIN_REGEX = re.compile("http(s|)://(www\.|)(.+?)(/.*|)$")


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


def _api_path(server_url: str) -> str:
    if server_url[-1] != '/':
        server_url += '/'
    return server_url + 'api/'


def _validate_server_url(server_url: str) -> None:
    if not DOMAIN_REGEX.match(server_url):
        raise ServerURLError(server_url)


def _check_connection(server_url: str) -> None:
    _validate_server_url(server_url)
    response = requests.get(_api_path(server_url) + 'help/test.json')
    if not response.json() == 'ok':
        raise requests.ConnectionError(server_url)


def _validate_credentials(server_url: str,
                          username: str,
                          password: str) -> None:
    are_valid = requests.get(
        _api_path(server_url) + 'account/verify_credentials.json',
        auth=HTTPBasicAuth(username, password)
    ).ok
    if not are_valid:
        raise AuthenticationError(server_url, username, password)


def _get_request(server_url: str,
                 resource_path: str,
                 credentials: Tuple[str, str]=None):
    resource_url = _api_path(server_url) + resource_path + '.json'
    if credentials:
        return requests.get(resource_url,
                            auth=HTTPBasicAuth(*credentials)).json()
    else:
        return requests.get(resource_url).json()


def statusnet_config(server_url: str) -> dict:
    return _get_request(server_url, 'statusnet/config')


def login(server_url: str, username: str, password: str) -> None:
    _check_connection(server_url)
    _validate_credentials(server_url, username, password)
