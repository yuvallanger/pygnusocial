"""
gnusocial.search
~~~~~~~~~~~~~~~~

Module with search resources.
"""
from dtd import docstring
from .utils import _get_request
from .docs import _SERVER_URL_DOC, _USERNAME_DOC, _PASSWORD_DOC, _STATUS_DICT


@docstring(server_url=_SERVER_URL_DOC,
           username=_USERNAME_DOC,
           password=_PASSWORD_DOC,
           status_dict=_STATUS_DICT)
def search(server_url: str,
           query: str,
           username: str='',
           password: str='') -> list:
    """Returns a collection of statuses matching a specified query.

:param str server_url: {server_url}
:param str query: UTF-8 encoded query
:param str username: (optional) {username}
:param str password: (optional) {password}
:rtype: list
:return: list of dicts with following structure:

::

    {status_dict}
    """
    return _get_request(server_url=server_url,
                        resource_path='search.json?q=%s' % query,
                        username=username,
                        password=password,
                        extension='').json()
