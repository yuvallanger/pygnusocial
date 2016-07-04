import pytest
from gnusocial.utils import _api_path, _validate_server_url, ServerURLError
from gnusocial.utils import _resource_url


SERVER_URL = 'https://gs.smuglo.li'


def test_api_path():
    valid_api_path = SERVER_URL + '/api/'
    assert _api_path(SERVER_URL) == valid_api_path
    assert _api_path(SERVER_URL + '/') == valid_api_path


def test_validate_server_url():
    with pytest.raises(ServerURLError):
        _validate_server_url(SERVER_URL[8:])


def test_resource_url():
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
