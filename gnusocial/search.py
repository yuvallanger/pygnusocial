from .utils import _get_request


def search(server_url: str,
           query: str,
           username: str='',
           password: str='') -> list:
    return _get_request(server_url=server_url,
                        resource_path='search.json?q=%s' % query,
                        username=username,
                        password=password,
                        extension='').json()
