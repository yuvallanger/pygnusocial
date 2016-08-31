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
           password: str='',
           **kwargs) -> list:
    """Returns a collection of statuses matching a specified query.

:param str server_url: {server_url}
:param str query: UTF-8 encoded query
:param str username: (optional) {username}
:param str password: (optional) {password}
:param int page: (optional) the page number (starting at 1) to return
:param int since_id: (optional) returns notices with ids greater than the
    given id
:param int rpp: (optional) the number of notices to return per page, up to a
    max of 100
:param str callback: if supplied when using the JSON format, the response will
    use the JSONP format with a callback of the given name
:rtype: list
:return: list of dicts with following structure:

::

    {status_dict}
    """
    return _get_request(server_url=server_url,
                        resource_path='search.json?q=%s' % query,
                        username=username,
                        password=password,
                        extension='',
                        params=kwargs).json()
