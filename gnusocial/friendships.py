"""
gnusocial.friendships
~~~~~~~~~~~~~~~~~~~~~

Module with friendship resources.
"""
from typing import Union
from dtd import docstring
from .utils import _post_request, _check_user_target
from .docs import (_SERVER_URL_DOC, _USERNAME_DOC, _PASSWORD_DOC, _USER_DICT,
                   _USER_ID_DOC, _SCREEN_NAME_DOC, _SOURCE_USER_DOC,
                   _TARGET_USER_DOC, _SOURCE_ID_DOC, _TARGET_ID_DOC,
                   _SOURCE_SCREEN_NAME_DOC, _TARGET_SCREEN_NAME_DOC,
                   _RELATIONSHIP_DICT)


@docstring(server_url=_SERVER_URL_DOC,
           username=_USERNAME_DOC,
           password=_PASSWORD_DOC,
           user_id=_USER_ID_DOC,
           screen_name=_SCREEN_NAME_DOC,
           user_dict=_USER_DICT)
def create(server_url: str,
           username: str,
           password: str,
           **kwargs) -> dict:
    """Allows the authenticating users to follow the user specified in the
user_id or screen_name parameter.

:param str server_url: {server_url}
:param str username: (optional) {username}
:param str password: (optional) {password}
:param int user_id: (optional) {user_id}
:param str screen_name: (optional) {screen_name}
:rtype: dict
:return: dict with following structure:

::

    {user_dict}
    """
    _check_user_target(**kwargs)
    return _post_request(server_url=server_url,
                         resource_path='friendships/create',
                         username=username,
                         password=password,
                         data=kwargs).json()


@docstring(server_url=_SERVER_URL_DOC,
           username=_USERNAME_DOC,
           password=_PASSWORD_DOC,
           user_id=_USER_ID_DOC,
           screen_name=_SCREEN_NAME_DOC,
           user_dict=_USER_DICT)
def destroy(server_url: str,
            username: str,
            password: str,
            **kwargs) -> dict:
    """Allows the authenticating users to unfollow the user specified in the
user_id or screen_name parameter.

:param str server_url: {server_url}
:param str username: (optional) {username}
:param str password: (optional) {password}
:param int user_id: (optional) {user_id}
:param str screen_name: (optional) {screen_name}
:rtype: dict
:return: dict with following structure:

::

    {user_dict}
    """
    _check_user_target(**kwargs)
    return _post_request(server_url=server_url,
                         resource_path='friendships/destroy',
                         username=username,
                         password=password,
                         data=kwargs).json()


@docstring(server_url=_SERVER_URL_DOC,
           username=_USERNAME_DOC,
           password=_PASSWORD_DOC,
           source_user=_SOURCE_USER_DOC,
           target_user=_TARGET_USER_DOC)
def exists(server_url: str,
           source_user: Union[str, int],
           target_user: Union[str, int],
           username: str='',
           password: str='') -> bool:
    """Shows if source_user follows target_user.

:param str server_url: {server_url}
:param source_user: User that is following. Can be an ID or screen name.
:type source_user: int or str
:param target_user: User that is followed. Can be an ID or screen name.
:type target_user: int or str
:param str username: (optional) {username}
:param str password: (optional) {password}
:rtype: bool
:return: `True` if `source_user` follows `target_user`. `False` otherwise.
    """
    data = {'user_a': source_user, 'user_b': target_user}
    return _post_request(server_url=server_url,
                         resource_path='friendships/exists',
                         username=username,
                         password=password,
                         data=data).json()


@docstring(server_url=_SERVER_URL_DOC,
           username=_USERNAME_DOC,
           password=_PASSWORD_DOC,
           source_id=_SOURCE_ID_DOC,
           source_screen_name=_SOURCE_SCREEN_NAME_DOC,
           target_id=_TARGET_ID_DOC,
           target_screen_name=_TARGET_SCREEN_NAME_DOC,
           relationship_dict=_RELATIONSHIP_DICT)
def show(server_url: str,
         username: str='',
         password: str='',
         **kwargs) -> dict:
    """Returns detailed information about the relationship between two
arbitrary users.

:param str server_url: {server_url}
:param str username: (optional) {username}
:param str password: (optional) {password}
:param int source_id: (optional) {source_id}
:param str source_screen_name: (optional) {source_screen_name}
:param int target_id: (optional) {target_id}
:param str target_screen_name: (optional) {target_screen_name}
:rtype: dict
:return: dict with following structure:

::

    {relationship_dict}
    """
    has_target_id = 'target_id' in kwargs
    has_target_screen_name = 'target_screen_name' in kwargs
    if has_target_id == has_target_screen_name:
        raise Exception(
            "You must either specify target_id or target_screen_name."
        )
    has_source_id = 'source_id' in kwargs
    has_source_screen_name = 'source_screen_name' in kwargs
    if has_source_id and has_source_screen_name:
        raise Exception(
            "You must either specify source_id or source_screen_name."
        )
    if (not has_source_id and not has_target_screen_name) and not username:
        raise Exception(
            "You must either specify source_id or " +
            "source_screen_name or username")
    return _post_request(server_url=server_url,
                         resource_path='friendships/show',
                         username=username,
                         password=password,
                         data=kwargs).json()
