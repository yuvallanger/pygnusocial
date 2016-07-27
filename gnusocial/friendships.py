"""
gnusocial.friendships
~~~~~~~~~~~~~~~~~~~~

Module with friendship resources.
"""
from typing import Union
from .utils import _post_request, _check_user_target, docstring
from .docs import (SERVER_URL_DOC, USERNAME_DOC, PASSWORD_DOC, USER_DICT,
                   USER_ID_DOC, SCREEN_NAME_DOC, SOURCE_USER_DOC,
                   TARGET_USER_DOC, SOURCE_ID_DOC, TARGET_ID_DOC,
                   SOURCE_SCREEN_NAME_DOC, TARGET_SCREEN_NAME_DOC,
                   RELATIONSHIP_DICT)


@docstring(server_url=SERVER_URL_DOC,
           username=USERNAME_DOC,
           password=PASSWORD_DOC,
           user_id=USER_ID_DOC,
           screen_name=SCREEN_NAME_DOC,
           user_dict=USER_DICT)
def create(server_url: str,
           username: str,
           password: str,
           **kwargs) -> dict:
    """Allows the authenticating users to follow the user specified in the
    user_id or screen_name parameter.

    :param server_url: {server_url}
    :param username: (optional) {username}
    :param password: (optional) {password}
    :param user_id: (optional) {user_id}
    :param screen_name: (optional) {screen_name}
    :return: dict with following structure:
        {user_dict}
    """
    _check_user_target(**kwargs)
    return _post_request(server_url=server_url,
                         resource_path='friendships/create',
                         username=username,
                         password=password,
                         data=kwargs).json()


@docstring(server_url=SERVER_URL_DOC,
           username=USERNAME_DOC,
           password=PASSWORD_DOC,
           user_id=USER_ID_DOC,
           screen_name=SCREEN_NAME_DOC,
           user_dict=USER_DICT)
def destroy(server_url: str,
            username: str,
            password: str,
            **kwargs) -> dict:
    """Allows the authenticating users to unfollow the user specified in the
    user_id or screen_name parameter.

    :param server_url: {server_url}
    :param username: (optional) {username}
    :param password: (optional) {password}
    :param user_id: (optional) {user_id}
    :param screen_name: (optional) {screen_name}
    :return: dict with following structure:
        {user_dict}
    """
    _check_user_target(**kwargs)
    return _post_request(server_url=server_url,
                         resource_path='friendships/destroy',
                         username=username,
                         password=password,
                         data=kwargs).json()


@docstring(server_url=SERVER_URL_DOC,
           username=USERNAME_DOC,
           password=PASSWORD_DOC,
           source_user=SOURCE_USER_DOC,
           target_user=TARGET_USER_DOC)
def exists(server_url: str,
           source_user: Union[str, int],
           target_user: Union[str, int],
           username: str='',
           password: str='') -> bool:
    """Shows if source_user follows target_user.

    :param server_url: {server_url}
    :param source_user: User that is following. Can be an ID or screen name.
    :param target_user: User that is followed. Can be an ID or screen name.
    :param username: (optional) {username}
    :param password: (optional) {password}
    :return: True if source_user follows target_user. False otherwise.
    """
    data = {'user_a': source_user, 'user_b': target_user}
    return _post_request(server_url=server_url,
                         resource_path='friendships/exists',
                         username=username,
                         password=password,
                         data=data).json()


@docstring(server_url=SERVER_URL_DOC,
           username=USERNAME_DOC,
           password=PASSWORD_DOC,
           source_id=SOURCE_ID_DOC,
           source_screen_name=SOURCE_SCREEN_NAME_DOC,
           target_id=TARGET_ID_DOC,
           target_screen_name=TARGET_SCREEN_NAME_DOC,
           relationship_dict=RELATIONSHIP_DICT)
def show(server_url: str,
         username: str='',
         password: str='',
         **kwargs) -> dict:
    """Returns detailed information about the relationship between two
    arbitrary users.

    :param server_url: {server_url}
    :param username: (optional) {username}
    :param password: (optional) {password}
    :param source_id: (optional) {source_id}
    :param source_screen_name: (optional) {source_screen_name}
    :param target_id: (optional) {target_id}
    :param target_screen_name: (optional) {target_screen_name}
    :return: dict with following structure:
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
