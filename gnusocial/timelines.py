"""
gnusocial.timelines
~~~~~~~~~~~~~~~~~~~

Module with timeline resources
"""
from .utils import _get_request, _check_user_target, docstring
from .docs import (_SERVER_URL_DOC, _USERNAME_DOC, _PASSWORD_DOC, _MAX_ID_DOC,
                   _SINCE_ID_DOC, _STATUSES_COUNT, _STATUS_DICT, _USER_ID_DOC,
                   _SCREEN_NAME_DOC)


@docstring(server_url=_SERVER_URL_DOC,
           username=_USERNAME_DOC,
           password=_PASSWORD_DOC,
           since_id=_SINCE_ID_DOC,
           max_id=_MAX_ID_DOC,
           count=_STATUSES_COUNT,
           status_dict=_STATUS_DICT)
def public(server_url: str,
           username: str='',
           password: str='',
           **kwargs) -> list:
    """Returns the most recent notices, including repeats if they exist, from
    non-protected users.

:param server_url: {server_url}
:param username: (optional) {username}
:param password: (optional) {password}
:param since_id: (optional) {since_id}
:param max_id: (optional) {max_id}
:param count: (optional) {count}
:return: list of dicts with following structure:

::

    {status_dict}
    """
    return _get_request(server_url=server_url,
                        resource_path='statuses/public_timeline',
                        username=username,
                        password=password,
                        params=kwargs).json()


@docstring(server_url=_SERVER_URL_DOC,
           username=_USERNAME_DOC,
           password=_PASSWORD_DOC,
           since_id=_SINCE_ID_DOC,
           max_id=_MAX_ID_DOC,
           count=_STATUSES_COUNT,
           status_dict=_STATUS_DICT)
def home(server_url: str, username: str, password: str, **kwargs) -> list:
    """Returns the most recent notices, including repeats if they exist,
    posted by the authenticating user and the users they follow. This is the
    same timeline seen by a user when they login to their instance.

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
    return _get_request(server_url=server_url,
                        resource_path='statuses/home_timeline',
                        username=username,
                        password=password,
                        params=kwargs).json()


@docstring(server_url=_SERVER_URL_DOC,
           username=_USERNAME_DOC,
           password=_PASSWORD_DOC,
           since_id=_SINCE_ID_DOC,
           max_id=_MAX_ID_DOC,
           count=_STATUSES_COUNT,
           status_dict=_STATUS_DICT,
           user_id=_USER_ID_DOC,
           screen_name=_SCREEN_NAME_DOC)
def friends(server_url: str,
            username: str='',
            password: str='',
            **kwargs) -> list:
    """Alias of statuses/home_timeline for the specified user.

:param server_url: {server_url}
:param username: (optional) {username}
:param password: (optional) {password}
:param since_id: (optional) {since_id}
:param max_id: (optional) {max_id}
:param count: (optional) {count}
:param user_id: (optional) {user_id}
:param screen_name: (optional) {screen_name}
:return: list of dicts with following structure:

::

    {status_dict}
    """
    _check_user_target(username, **kwargs)
    return _get_request(server_url=server_url,
                        resource_path='statuses/friends_timeline',
                        username=username,
                        password=password,
                        params=kwargs).json()


@docstring(server_url=_SERVER_URL_DOC,
           username=_USERNAME_DOC,
           password=_PASSWORD_DOC,
           since_id=_SINCE_ID_DOC,
           max_id=_MAX_ID_DOC,
           count=_STATUSES_COUNT,
           status_dict=_STATUS_DICT,
           user_id=_USER_ID_DOC,
           screen_name=_SCREEN_NAME_DOC)
def user(server_url: str,
         username: str='',
         password: str='',
         **kwargs) -> list:
    """Returns the most recent notices posted by the authenticating user. It
    is also possible to request another user's timeline by using the
    screen_name or user_id parameter. The other users timeline will only be
    visible if they are not protected, or if the authenticating user's follow
    request was accepted by the protected user.

:param server_url: {server_url}
:param username: (optional) {username}
:param password: (optional) {password}
:param since_id: (optional) {since_id}
:param max_id: (optional) {max_id}
:param count: (optional) {count}
:param user_id: (optional) {user_id}
:param screen_name: (optional) {screen_name}
:return: list of dicts with following structure:

::

    {status_dict}
    """
    _check_user_target(username, **kwargs)
    return _get_request(server_url=server_url,
                        resource_path='statuses/user_timeline',
                        username=username,
                        password=password,
                        params=kwargs).json()


@docstring(server_url=_SERVER_URL_DOC,
           username=_USERNAME_DOC,
           password=_PASSWORD_DOC,
           since_id=_SINCE_ID_DOC,
           max_id=_MAX_ID_DOC,
           count=_STATUSES_COUNT,
           status_dict=_STATUS_DICT,
           user_id=_USER_ID_DOC,
           screen_name=_SCREEN_NAME_DOC)
def mentions(server_url: str,
             username: str='',
             password: str='',
             **kwargs) -> list:
    """Returns the most recent mentions (notices containing @username) for
    the authenticating user or specified user.

:param server_url: {server_url}
:param username: (optional) {username}
:param password: (optional) {password}
:param since_id: (optional) {since_id}
:param max_id: (optional) {max_id}
:param count: (optional) {count}
:param user_id: (optional) {user_id}
:param screen_name: (optional) {screen_name}
:return: list of dicts with following structure:

::

    {status_dict}
    """
    _check_user_target(username, **kwargs)
    return _get_request(server_url=server_url,
                        resource_path='statuses/mentions',
                        username=username,
                        password=password,
                        params=kwargs).json()


@docstring(server_url=_SERVER_URL_DOC,
           username=_USERNAME_DOC,
           password=_PASSWORD_DOC,
           since_id=_SINCE_ID_DOC,
           max_id=_MAX_ID_DOC,
           count=_STATUSES_COUNT,
           status_dict=_STATUS_DICT,
           user_id=_USER_ID_DOC,
           screen_name=_SCREEN_NAME_DOC)
def replies(server_url: str,
            username: str='',
            password: str='',
            **kwargs) -> list:
    """Alias of statuses/mentions

:param server_url: {server_url}
:param username: (optional) {username}
:param password: (optional) {password}
:param since_id: (optional) {since_id}
:param max_id: (optional) {max_id}
:param count: (optional) {count}
:param user_id: (optional) {user_id}
:param screen_name: (optional) {screen_name}
:return: list of dicts with following structure:

::

    {status_dict}
    """
    _check_user_target(username, **kwargs)
    return _get_request(server_url=server_url,
                        resource_path='statuses/replies',
                        username=username,
                        password=password,
                        params=kwargs).json()
