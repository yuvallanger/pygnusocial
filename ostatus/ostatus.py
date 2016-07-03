import re
import requests

domain_regex = re.compile("http(s|)://(www\.|)(.+?)(/.*|)$")


class ServerURLError(Exception):
    def __init__(self, server_url: str):
        self.server_url = server_url

    def __repr__(self):
        return 'ServerURLError(%r)' % self.server_url

    def __str__(self):
        return 'Invalid server URL %s' % self.server_url


class AuthenticationError(Exception):
    def __init__(self, server_url: str, username: str, password: str):
        self.server_url = server_url
        self.username = username
        self.password = password

    @property
    def credentials(self):
        return (self.username, self.password)

    def __repr__(self):
        return 'AuthenticationError(%r, %r, %r)' % (self.server_url,
                                                    *self.credentials)

    def __str__(self):
        return 'Invalid credentials %s:%s for %s' % (*self.credentials,
                                                     self.server_url)


def _api_path(server_url: str) -> str:
    if server_url[-1] != '/':
        server_url += '/'
    return server_url + 'api/'


def _validate_server_url(server_url: str):
    if not domain_regex.match(server_url):
        raise ServerURLError(server_url)


def _check_connection(server_url: str):
    _validate_server_url(server_url)
    response = requests.get(_api_path(server_url) + 'help/test.json')
    if not response.json() == 'ok':
        raise requests.ConnectionError(server_url)


def get_request(server_url: str, resource_path: str) -> dict:
    _check_connection(server_url)
    return requests.get(_api_path(server_url) +
                        resource_path + '.json').json()
