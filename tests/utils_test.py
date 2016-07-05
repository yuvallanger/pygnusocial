"""Unit tests for gnusocial.utils module."""
import pytest
from gnusocial.utils import _api_path, _validate_server_url, ServerURLError
from gnusocial.utils import _resource_url


SERVER_URL = 'https://gs.smuglo.li'


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
