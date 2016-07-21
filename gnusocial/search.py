"""
gnusocial.search
~~~~~~~~~~~~~~~~

Module with search resources.
"""
from .utils import _get_request


def search(server_url: str,
           query: str,
           username: str='',
           password: str='') -> list:
    """Returns a collection of statuses matching a specified query.

    :param server_url: URL of the server
    :param query: UTF-8 encoded query
    :param username: (optional) name of the authenticating user
    :param password: (optional) password of the authenticating user
    :return: list of post dicts.
    """
    return _get_request(server_url=server_url,
                        resource_path='search.json?q=%s' % query,
                        username=username,
                        password=password,
                        extension='').json()
