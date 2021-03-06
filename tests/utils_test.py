"Unit tests for gnusocial.utils module."
from functools import partial
import pytest
import requests
from requests.models import Response
from gnusocial.utils import (
    _api_path, _validate_server_url, ServerURLError, _resource_url,
    _check_connection, _get_request, AuthenticationError, _post_request,
    _check_auth_error, GNUSocialAPIError
)
from conftest import (
    SERVER_URL, RESPONSE_STRING, USERNAME, PASSWORD, ERROR_STRING
)


def test_api_path():
    """Test function for gnusocial.utils._api_path function.
    It should return a server URL string with 'api/' or '/api/' added
    if there is a trailing slash or there is none respectively.
    """
    valid_api_path = SERVER_URL + '/api/'
    assert _api_path(SERVER_URL) == valid_api_path
    assert _api_path(SERVER_URL + '/') == valid_api_path


def test_validate_server_url():
    """Test function for gnusocial.utils._validate_server_url function.
    It should raise a gnusocial.utils.ServerURLError exception
    if given invalid server URL.
    It should return None if everything is fine.
    """
    assert _validate_server_url(SERVER_URL) is None
    with pytest.raises(ServerURLError):
        _validate_server_url(SERVER_URL[8:])


def test_resource_url():
    """Test function for gnusocial.utils._resource_url function.
    It should return '_api_path(server_url) + resource_path +
    extension' string.
    Extenstion defaults to '.as'.
    """
    resource_path = 'help/test'
    extension = '.as'
    valid_resource_url = _api_path(SERVER_URL) + resource_path + '.json'
    valid_resource_url_as = _api_path(SERVER_URL) + resource_path + extension
    assert _resource_url(
        server_url=SERVER_URL,
        resource_path=resource_path) == valid_resource_url
    assert _resource_url(
        server_url=SERVER_URL,
        resource_path=resource_path,
        extension=extension) == valid_resource_url_as


def test_get_request():
    """Test function for gnusocial.utils._get_request function.
    Any request to '/get' resource path should return 'Hello world!'
    """
    credentials = {'username': USERNAME, 'password': PASSWORD}
    invalid_credentials = {'username': 'test', 'password': 'test'}
    get = partial(_get_request, server_url=SERVER_URL, resource_path='get')
    get_auth = partial(_get_request,
                       server_url=SERVER_URL,
                       resource_path='get_auth')
    assert get() == RESPONSE_STRING
    assert get(extension='.json') == RESPONSE_STRING
    assert get_auth(**credentials) == RESPONSE_STRING
    assert get_auth(extension='.json', **credentials) == \
        RESPONSE_STRING
    with pytest.raises(AuthenticationError):
        get_auth(**invalid_credentials)
        get_auth(extension='.json', **invalid_credentials)
    with pytest.raises(GNUSocialAPIError) as excinfo:
        _get_request(server_url=SERVER_URL, resource_path='get_error')
    assert ERROR_STRING == excinfo.value.error_message


def test_check_connection():
    """Test function for gnusocial.utils._check_connection function.
    It should raise requests.ConnectionError if
    connection to server is not established.
    It should return None if everything is fine.
    """
    with pytest.raises(requests.ConnectionError):
        _check_connection(SERVER_URL[:-1])
    assert _check_connection(SERVER_URL) is None


def test_post_request():
    """Test function for gnusocial.utils._post_request function.
    Any request to '/post' resource path should return 'Hello world!'
    """
    post = partial(_post_request, SERVER_URL, 'post', username=USERNAME, data={})
    assert post(password=PASSWORD) == RESPONSE_STRING
    with pytest.raises(AuthenticationError):
        post(password=PASSWORD[:-1])
    with pytest.raises(GNUSocialAPIError) as excinfo:
        _post_request(server_url=SERVER_URL, resource_path='post_error')
    assert ERROR_STRING == excinfo.value.error_message


def test_check_auth_error():
    """Test function for gnusocial.utils._check_auth_error function.
    It should raise an AuthenticationError if response.status_code equals 401.
    """
    check_auth = partial(_check_auth_error,
                         server_url=SERVER_URL,
                         username=USERNAME)
    ok_response = Response()
    ok_response.status_code = 200
    auth_error = Response()
    auth_error.status_code = 401
    assert check_auth(ok_response) is None
    with pytest.raises(AuthenticationError):
        check_auth(auth_error)
