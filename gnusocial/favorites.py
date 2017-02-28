"""
gnusocial.favorites
~~~~~~~~~~~~~~~~~~~

Module with favorite resources.
"""
from dtd import docstring
from .utils import _post_request, _check_user_target
from .docs import (_SERVER_URL_DOC, _USERNAME_DOC, _PASSWORD_DOC,
                   _SINCE_ID_DOC, _MAX_ID_DOC, _STATUSES_COUNT, _STATUS_DICT,
                   _STATUS_ID_DOC, _USER_ID_DOC, _SCREEN_NAME_DOC)


@docstring(server_url=_SERVER_URL_DOC,
           username=_USERNAME_DOC,
           password=_PASSWORD_DOC,
           since_id=_SINCE_ID_DOC,
           max_id=_MAX_ID_DOC,
           count=_STATUSES_COUNT,
           status_dict=_STATUS_DICT,
           user_id=_USER_ID_DOC,
           screen_name=_SCREEN_NAME_DOC)
def favorites(server_url: str,
              username: str,
              password: str,
              **kwargs) -> list:
    """Returns the 20 most recent notices favorited by the authenticating or
specified user.

:param str server_url: {server_url}
:param str username: {username}
:param str password: {password}
:param int since_id: (optional) {since_id}
:param int max_id: (optional) {max_id}
:param int count: (optional) {count}
:param int user_id: (optional) {user_id}
:param str screen_name: (optional) {screen_name}
:rtype: list
:return: list of dicts with following structure:

::

    {status_dict}
    """
    _check_user_target(username, use_username=True, **kwargs)
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

:param str server_url: {server_url}
:param str username: {username}
:param str password: {password}
:param int status_id: {status_id}
:rtype: dict
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

:param str server_url: {server_url}
:param str username: {username}
:param str password: {password}
:param int status_id: {status_id}
:rtype: dict
:return: dict with following structure:

::

    {status_dict}
    """
    return _post_request(server_url=server_url,
                         resource_path='favorites/destroy/%d' % status_id,
                         username=username,
                         password=password).json()
