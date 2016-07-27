"""
gnusocial.blocks
~~~~~~~~~~~~~~~~

Module with block resources.
"""
from .utils import _post_request, _check_user_target, docstring
from .docs import (SERVER_URL_DOC, USERNAME_DOC, PASSWORD_DOC, USER_DICT,
                   USER_ID_DOC, SCREEN_NAME_DOC)


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
    """Blocks the specified user from following the authenticating user.
    In addition the blocked user will not show in the authenticating users
    mentions or timeline (unless repeated by another user). If a follow or
    friend relationship exists it is destroyed.

    :param server_url: {server_url}
    :param username: {username}
    :param password: {password}
    :param user_id: (optional) {user_id}
    :param screen_name: (optional) {screen_name}
    :return: dict with following structure:
        {user_dict}
    """
    _check_user_target(**kwargs)
    return _post_request(server_url=server_url,
                         resource_path='blocks/create',
                         username=username,
                         password=password,
                         data=kwargs).json()


@docstring(SERVER_URL_DOC, USERNAME_DOC, PASSWORD_DOC, USER_ID_DOC,
           SCREEN_NAME_DOC, USER_DICT)
def destroy(server_url: str,
            username: str,
            password: str,
            **kwargs) -> dict:
    """Un-blocks the specified user from following the authenticating user.
     If relationships existed before the block was instated,
     they will not be restored.

    :param server_url: {server_url}
    :param username: {username}
    :param password: {password}
    :param user_id: (optional) {user_id}
    :param screen_name: (optional) {screen_name}
    :return: dict with following structure:
        {user_dict}
    """
    _check_user_target(**kwargs)
    return _post_request(server_url=server_url,
                         resource_path='blocks/destroy',
                         username=username,
                         password=password,
                         data=kwargs).json()
