"""
gnusocial.friends
~~~~~~~~~~~~~~~~~

Module with friends resources.
"""
from typing import List
from .utils import _post_request, _check_user_target, docstring
from .docs import (SERVER_URL_DOC, USERNAME_DOC, PASSWORD_DOC, SINCE_ID_DOC,
                   USER_ID_DOC, SCREEN_NAME_DOC, USERS_COUNT, MAX_ID_DOC)


@docstring(server_url=SERVER_URL_DOC,
           username=USERNAME_DOC,
           password=PASSWORD_DOC,
           user_id=USER_ID_DOC,
           screen_name=SCREEN_NAME_DOC,
           count=USERS_COUNT,
           since_id=SINCE_ID_DOC,
           max_id=MAX_ID_DOC)
def friends(server_url: str,
            username: str='',
            password: str='',
            **kwargs) -> List[int]:
    """Returns IDs of users the auntenticated or
    specified user is following (otherwise known as their "friends").

    :param server_url: {server_url}
    :param username: (optional) {username}
    :param password: (optional) {password}
    :param user_id: (optional) {user_id}
    :param screen_name: (optional) {screen_name}
    :param count: (optional) {count}
    :param since_id: (optional) {since_id}
    :param max_id: (optional) {max_id}
    :return: a list of user IDs
    """
    _check_user_target(username, **kwargs)
    return _post_request(server_url=server_url,
                         resource_path='friends/ids',
                         username=username,
                         password=password,
                         data=kwargs).json()


@docstring(server_url=SERVER_URL_DOC,
           username=USERNAME_DOC,
           password=PASSWORD_DOC,
           user_id=USER_ID_DOC,
           screen_name=SCREEN_NAME_DOC,
           count=USERS_COUNT,
           since_id=SINCE_ID_DOC,
           max_id=MAX_ID_DOC)
def followers(server_url: str,
              username: str='',
              password: str='',
              **kwargs) -> List[int]:
    """Returns IDs of users the auntenticated or
    specified user is followed by (otherwise known as their "friends").

    :param server_url: {server_url}
    :param username: (optional) {username}
    :param password: (optional) {password}
    :param user_id: (optional) {user_id}
    :param screen_name: (optional) {screen_name}
    :param count: (optional) {count}
    :param since_id: (optional) {since_id}
    :param max_id: (optional) {max_id}
    :return: a list of user IDs
    """
    _check_user_target(username, **kwargs)
    return _post_request(server_url=server_url,
                         resource_path='followers/ids',
                         username=username,
                         password=password,
                         data=kwargs).json()
