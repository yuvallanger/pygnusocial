"""
gnusocial.friends
~~~~~~~~~~~~~~~~~

Module with friends resources.
"""
from typing import List
from dtd import docstring
from .utils import _post_request, _check_user_target
from .docs import (_SERVER_URL_DOC, _USERNAME_DOC, _PASSWORD_DOC, _MAX_ID_DOC,
                   _USER_ID_DOC, _SCREEN_NAME_DOC, _USERS_COUNT, _SINCE_ID_DOC)


@docstring(server_url=_SERVER_URL_DOC,
           username=_USERNAME_DOC,
           password=_PASSWORD_DOC,
           user_id=_USER_ID_DOC,
           screen_name=_SCREEN_NAME_DOC,
           count=_USERS_COUNT,
           since_id=_SINCE_ID_DOC,
           max_id=_MAX_ID_DOC)
def friends(server_url: str,
            username: str='',
            password: str='',
            **kwargs) -> List[int]:
    """Returns IDs of users the auntenticated or
specified user is following (otherwise known as their "friends").

:param str server_url: {server_url}
:param str username: (optional) {username}
:param str password: (optional) {password}
:param int user_id: (optional) {user_id}
:param str screen_name: (optional) {screen_name}
:param int count: (optional) {count}
:param int since_id: (optional) {since_id}
:param int max_id: (optional) {max_id}
:rtype: list
:return: a list of user IDs
    """
    _check_user_target(username, **kwargs)
    return _post_request(server_url=server_url,
                         resource_path='friends/ids',
                         username=username,
                         password=password,
                         data=kwargs).json()


@docstring(server_url=_SERVER_URL_DOC,
           username=_USERNAME_DOC,
           password=_PASSWORD_DOC,
           user_id=_USER_ID_DOC,
           screen_name=_SCREEN_NAME_DOC,
           count=_USERS_COUNT,
           since_id=_SINCE_ID_DOC,
           max_id=_MAX_ID_DOC)
def followers(server_url: str,
              username: str='',
              password: str='',
              **kwargs) -> List[int]:
    """Returns IDs of users the auntenticated or
specified user is followed by (otherwise known as their "friends").

:param str server_url: {server_url}
:param str username: (optional) {username}
:param str password: (optional) {password}
:param int user_id: (optional) {user_id}
:param str screen_name: (optional) {screen_name}
:param int count: (optional) {count}
:param int since_id: (optional) {since_id}
:param int max_id: (optional) {max_id}
:rtype: list
:return: a list of user IDs
    """
    _check_user_target(username, **kwargs)
    return _post_request(server_url=server_url,
                         resource_path='followers/ids',
                         username=username,
                         password=password,
                         data=kwargs).json()
