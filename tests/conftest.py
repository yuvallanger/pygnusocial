"""Global constants for tests."""
from os.path import dirname, abspath, join
from json import loads
import pytest
from parse import parse
from requests import ConnectionError
CURDIR = dirname(abspath(__file__))
SERVER_URL = 'http://127.0.0.1:5000'
RESPONSE_STRING = 'Hello world!'
USERNAME = 'admin'
PASSWORD = 'secret'


def verify_credentials(**kwargs):
    auth = kwargs.pop('auth')
    if auth == (USERNAME, PASSWORD):
        return 200
    else:
        return 401


def get_response_filename(filename):
    return join(CURDIR, 'responses', filename)


def connection(**kwargs):
    if kwargs.pop('server_url') != SERVER_URL:
        raise ConnectionError()


CODES = {
    'get_auth.json': verify_credentials,
    'post.json': verify_credentials,
    'account/verify_credentials.json': verify_credentials,
}


def get_resource_path(url):
    result = parse('{server_url}/api/{path}', url)
    if result['server_url'] != SERVER_URL:
        raise ConnectionError()
    if 'path' in result.named:
        return result['path']


def get_response_text(resource_path):
    filename = get_response_filename(resource_path)
    return open(filename).read()


class Response(object):
    def __init__(self, url=None, params=None, auth=None, files=None,
                 data=None, json=None):
        resource_path = get_resource_path(url)
        self.text = get_response_text(resource_path)
        result = CODES.get(resource_path, 200)
        self.status_code = result
        if result != 200:
            self.status_code = result(params=params, auth=auth, files=files,
                                      data=data)

    def json(self):
        return loads(self.text)


def get(url, params=None, **kwargs):
    return Response(url=url, params=params, **kwargs)


def post(url, data=None, json=None, **kwargs):
    return Response(url=url, data=data, json=json, **kwargs)


@pytest.fixture(autouse=True)
def no_requests(monkeypatch):
    monkeypatch.setattr('requests.get', get)
    monkeypatch.setattr('requests.post', post)
