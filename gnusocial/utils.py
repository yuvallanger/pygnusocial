import re
from functools import partial
import requests

from .exceptions import AuthenticationError, ServerURLError, GNUSocialAPIError

DOMAIN_REGEX = re.compile(r"http(s|)://(www\.|)(.+?)(/.*|)$")


def _check_auth_error(response, server_url, username, password):
    if response.status_code == 401:
        raise AuthenticationError(server_url, username, password)


def _api_path(server_url):
    _validate_server_url(server_url)
    if server_url[-1] != '/':
        server_url += '/'
    return server_url + 'api/'


def _validate_server_url(server_url):
    if not DOMAIN_REGEX.match(server_url):
        raise ServerURLError(server_url)


def _check_connection(server_url):
    response = _get_request(server_url, 'help/test').json()
    if response != 'ok':
        raise requests.ConnectionError(server_url)


def _resource_url(server_url, resource_path, extension='.json'):
    return _api_path(server_url) + resource_path + extension


def _request(request_func, server_url, resource_path, **kwargs):
    extension = kwargs.get('extension', '.json')
    req = partial(request_func,
                  url=_resource_url(server_url, resource_path, extension),
                  data=kwargs.get('data'),
                  files=kwargs.get('files'),
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
        return response_json
    return response


def _get_request(server_url, resource_path, **kwargs):
    return _request(requests.get, server_url, resource_path, **kwargs)


def _post_request(server_url, resource_path, **kwargs):
    return _request(requests.post, server_url, resource_path, **kwargs)
