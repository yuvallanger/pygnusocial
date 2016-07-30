"""
gnusocial.favorites
~~~~~~~~~~~~~~~~~~~

Module with favorite resources.
"""
from .utils import _post_request, _check_user_target, docstring
from .docs import (_SERVER_URL_DOC, _USERNAME_DOC, _PASSWORD_DOC,
                   _SINCE_ID_DOC, _MAX_ID_DOC, _STATUSES_COUNT, _STATUS_DICT,
                   _STATUS_ID_DOC)


@docstring(server_url=_SERVER_URL_DOC,
           username=_USERNAME_DOC,
           password=_PASSWORD_DOC,
           since_id=_SINCE_ID_DOC,
           max_id=_MAX_ID_DOC,
           count=_STATUSES_COUNT,
           status_dict=_STATUS_DICT)
def favorites(server_url: str,
              username: str,
              password: str,
              **kwargs) -> list:
    """Returns the 20 most recent notices favorited by the authenticating or
    specified user.

:param server_url: {server_url}
:param username: {username}
:param password: {password}
:param since_id: (optional) {since_id}
:param max_id: (optional) {max_id}
:param count: (optional) {count}
:return: list of dicts with following structure:

::

    {status_dict}
    """
    _check_user_target(**kwargs)
    return _post_request(server_url=server_url,
                         resource_path='favorites',
                         username=username,
                         password=password,
                         data=kwargs).json()


@docstring(server_url=_SERVER_URL_DOC,
           username=_USERNAME_DOC,
           password=_PASSWORD_DOC,
           status_id=_STATUS_ID_DOC,
           status_dict=_STATUS_DICT)
def create(server_url: str,
           username: str,
           password: str,
           status_id: int) -> dict:
    """Favorites the status specified in the ID parameter as the
    authenticating user. Returns the liked status when successful.

:param server_url: {server_url}
:param username: {username}
:param password: {password}
:param status_id: {status_id}
:return: dict with following structure:

::

    {status_dict}
    """
    return _post_request(server_url=server_url,
                         resource_path='favorites/create/%d' % status_id,
                         username=username,
                         password=password).json()


@docstring(server_url=_SERVER_URL_DOC,
           username=_USERNAME_DOC,
           password=_PASSWORD_DOC,
           status_id=_STATUS_ID_DOC,
           status_dict=_STATUS_DICT)
def destroy(server_url: str,
            username: str,
            password: str,
            status_id: int) -> dict:
    """Unfavorites the status specified in the ID parameter as the
    authenticating user. Returns the unliked status when successful.

:param server_url: {server_url}
:param username: {username}
:param password: {password}
:param status_id: {status_id}
:return: dict with following structure:

::

    {status_dict}
    """
    return _post_request(server_url=server_url,
                         resource_path='favorites/destroy/%d' % status_id,
                         username=username,
                         password=password).json()
