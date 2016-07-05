"""Unit tests for gnusocial.utils module."""
from functools import partial
import pytest
import requests
from gnusocial.utils import _api_path, _validate_server_url, ServerURLError
from gnusocial.utils import _resource_url, _check_connection
from gnusocial.utils import _get_request
from conftest import SERVER_URL


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
    if given invalid server URL."""
    with pytest.raises(ServerURLError):
        _validate_server_url(SERVER_URL[8:])


def test_resource_url():
    """Test function for gnusocial.utils._resource_url function.
    It should return '_api_path(server_url) + resource_path +
    extension' string.
    Extenstion defaults to '.as'."""
    resource_path = 'help/test'
    extension = '.json'
    valid_resource_url = _api_path(SERVER_URL) + resource_path + extension
    valid_resource_url_as = _api_path(SERVER_URL) + resource_path + '.as'
    assert _resource_url(
        server_url=SERVER_URL,
        resource_path=resource_path,
        extension=extension) == valid_resource_url
    assert _resource_url(
        server_url=SERVER_URL,
        resource_path=resource_path) == valid_resource_url_as


def test_get_request():
    """Test function for gnusocial.utils._get_request function.
    The test server is configured that way, that
    _get_request(SERVER_URL, 'get') should return 'Hello world!'
    and _get_request(SERVER_URL, 'get', extension='.json')
    should return {'Hello': 'world'}.
    """
    get = partial(_get_request, server_url=SERVER_URL, resource_path='get')
    assert get() == 'Hello world!'
    assert get(extension='.json') == {'Hello': 'world'}


def test_check_connection():
    """Test function for gnusocial.utils._check_connection function.
    It should raise requests.ConnectionError if
    connection to server is not established.
    It should return None is everything is fine."""
    with pytest.raises(requests.ConnectionError):
        _check_connection(SERVER_URL[:-1])
    assert _check_connection(SERVER_URL) is None
