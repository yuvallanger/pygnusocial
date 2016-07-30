"""
gnusocial.users
~~~~~~~~~~~~~~~

Module with user resources.
"""
from .utils import _get_request, _check_user_target, docstring
from .docs import (_SERVER_URL_DOC, _USERNAME_DOC, _PASSWORD_DOC, _USER_DICT,
                   _USER_ID_DOC, _SCREEN_NAME_DOC, _USERS_COUNT)


@docstring(server_url=_SERVER_URL_DOC,
           username=_USERNAME_DOC,
           password=_PASSWORD_DOC,
           user_id=_USER_ID_DOC,
           screen_name=_SCREEN_NAME_DOC,
           count=_USERS_COUNT,
           user_dict=_USER_DICT)
def following(server_url: str,
              username: str='',
              password: str='',
              **kwargs) -> list:
    """Returns a collection of user objects for users followed by
    the specified user.

:param server_url: {server_url}
:param username: (optional) {username}
:param password: (optional) {password}
:param user_id: (optional) {user_id}
:param screen_name: (optional) {screen_name}
:param count: (optional) {count}
:return: a list of dicts with following sctructure:

::

    {user_dict}
    """
    _check_user_target(username, **kwargs)
    return _get_request(server_url=server_url,
                        resource_path='statuses/friends',
                        username=username,
                        password=password,
                        params=kwargs).json()


@docstring(server_url=_SERVER_URL_DOC,
           username=_USERNAME_DOC,
           password=_PASSWORD_DOC,
           user_id=_USER_ID_DOC,
           screen_name=_SCREEN_NAME_DOC,
           count=_USERS_COUNT,
           user_dict=_USER_DICT)
def followers(server_url: str,
              username: str='',
              password: str='',
              **kwargs) -> list:
    """Returns a collection of user objects for users following
    the specified user.

:param server_url: {server_url}
:param username: (optional) {username}
:param password: (optional) {password}
:param user_id: (optional) {user_id}
:param screen_name: (optional) {screen_name}
:param count: (optional) {count}
:return: a list of dicts with following sctructure:

::

    {user_dict}
    """
    _check_user_target(username, **kwargs)
    return _get_request(server_url=server_url,
                        resource_path='statuses/followers',
                        username=username,
                        password=password,
                        params=kwargs).json()


@docstring(server_url=_SERVER_URL_DOC,
           username=_USERNAME_DOC,
           password=_PASSWORD_DOC,
           user_id=_USER_ID_DOC,
           screen_name=_SCREEN_NAME_DOC,
           user_dict=_USER_DICT)
def show(server_url: str,
         username: str='',
         password: str='',
         **kwargs):
    """Returns a variety of information about the user specified by the
    required user_id or screen_name parameter. The author’s most recent
    status will be returned inline when possible.

:param server_url: {server_url}
:param username: (optional) {username}
:param password: (optional) {password}
:param user_id: (optional) {user_id}
:param screen_name: (optional) {screen_name}
:return: dict with following sctructure:

::

    {user_dict}
    """
    _check_user_target(username, **kwargs)
    return _get_request(server_url=server_url,
                        resource_path='users/show',
                        username=username,
                        password=password,
                        params=kwargs).json()
