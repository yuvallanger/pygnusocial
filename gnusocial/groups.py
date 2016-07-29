"""
gnusocial.groups
~~~~~~~~~~~~~~~~

Module with group resources.
"""
from .utils import (_post_request, _get_request, docstring,
                    _check_user_target, _check_group_id_and_name,
                    _check_id_and_nickname)
from .docs import (SERVER_URL_DOC, USERNAME_DOC, PASSWORD_DOC, USER_DICT,
                   USER_ID_DOC, SCREEN_NAME_DOC, GROUP_COUNT, STATUS_DICT,
                   GROUP_ID_DOC, GROUP_NAME_DOC, MAX_ID_DOC, SINCE_ID_DOC,
                   GROUP_DICT, GROUP_DESCRIPTION, GROUP_LOCATION,
                   ALIASES_DOC, HOMEPAGE_DOC, FULLNAME_DOC, USERS_COUNT)


def _resource_path(resource_path: str, **kwargs) -> str:
    _check_id_and_nickname(**kwargs)
    group_id = kwargs.get('id')
    group_name = kwargs.get('nickname')
    if group_id:
        resource_path += '/%d' % group_id
    if group_name:
        resource_path += '/%s' % group_name
    return resource_path


@docstring(server_url=SERVER_URL_DOC,
           username=USERNAME_DOC,
           password=PASSWORD_DOC,
           id=GROUP_ID_DOC,
           nickname=GROUP_NAME_DOC,
           count=GROUP_COUNT,
           since_id=SINCE_ID_DOC,
           max_id=MAX_ID_DOC,
           status_dict=STATUS_DICT)
def timeline(server_url: str,
             username: str='',
             password: str='',
             **kwargs) -> list:
    """Shows a group's timeline. Similar to other timeline resources.

    :param server_url: {server_url}
    :param username: (optional) {username}
    :param password: (optional) {password}
    :param id: (optional) {id}
    :param nickname: (optional) {nickname}
    :param since_id: (optional) {since_id}
    :param max_id: (optional) {max_id}
    :param count: (optional) {count}
    :return: list of dicts with following sctructure:
        {status_dict}
    """
    resource_path = _resource_path('statusnet/groups/timeline', **kwargs)
    return _post_request(server_url=server_url,
                         resource_path=resource_path,
                         username=username,
                         password=password,
                         data=kwargs).json()


@docstring(server_url=SERVER_URL_DOC,
           username=USERNAME_DOC,
           password=PASSWORD_DOC,
           id=GROUP_ID_DOC,
           nickname=GROUP_NAME_DOC,
           group_dict=GROUP_DICT)
def show(server_url: str,
         username: str='',
         password: str='',
         **kwargs) -> dict:
    """Show a group's profile.

    :param server_url: {server_url}
    :param username: (optional) {username}
    :param password: (optional) {password}
    :param id: (optional) {id}
    :param nickname: (optional) {nickname}
    :return: dict with following sctructure:
        {group_dict}
    """
    resource_path = _resource_path('statusnet/groups/show', **kwargs)
    return _get_request(server_url=server_url,
                        resource_path=resource_path,
                        username=username,
                        password=password,
                        params=kwargs).json()


@docstring(server_url=SERVER_URL_DOC,
           username=USERNAME_DOC,
           password=PASSWORD_DOC,
           full_name=FULLNAME_DOC,
           homepage=HOMEPAGE_DOC,
           description=GROUP_DESCRIPTION,
           location=GROUP_LOCATION,
           aliases=ALIASES_DOC,
           group_dict=GROUP_DICT)
def create(server_url: str,
           username: str,
           password: str,
           **kwargs) -> dict:
    """Create a new group.

    :param server_url: {server_url}
    :param username: {username}
    :param password: {password}
    :param nickname: the name of the new group
    :param full_name: (optional) {full_name}
    :param homepage: (optional) {homepage}
    :param description: (optional) {description}
    :param location: (optional) {location}
    :param aliases: (optional) {aliases}
    :return: dict with following sctructure:
        {group_dict}
    """
    if 'nickname' not in kwargs:
        raise Exception(
            'You must specify the nickname of the new group.'
        )
    return _post_request(server_url=server_url,
                         resource_path='statusnet/groups/create',
                         username=username,
                         password=password,
                         data=kwargs).json()


@docstring(server_url=SERVER_URL_DOC,
           username=USERNAME_DOC,
           password=PASSWORD_DOC,
           id=GROUP_ID_DOC,
           nickname=GROUP_NAME_DOC,
           group_dict=GROUP_DICT)
def join(server_url: str,
         username: str,
         password: str,
         **kwargs) -> dict:
    """Join a group.

    :param server_url: {server_url}
    :param username: {username}
    :param password: {password}
    :param id: (optional) {id}
    :param nickname: (optional) {nickname}
    :return: dict with following sctructure:
        {group_dict}
    """
    resource_path = _resource_path('statusnet/groups/join', **kwargs)
    return _post_request(server_url=server_url,
                         resource_path=resource_path,
                         username=username,
                         password=password,
                         data=kwargs).json()


@docstring(server_url=SERVER_URL_DOC,
           username=USERNAME_DOC,
           password=PASSWORD_DOC,
           id=GROUP_ID_DOC,
           nickname=GROUP_NAME_DOC,
           group_dict=GROUP_DICT)
def leave(server_url: str,
          username: str,
          password: str,
          **kwargs) -> dict:
    """Leave a group.

    :param server_url: {server_url}
    :param username: {username}
    :param password: {password}
    :param id: (optional) {id}
    :param nickname: (optional) {nickname}
    :return: dict with following sctructure:
        {group_dict}
    """
    resource_path = _resource_path('statusnet/groups/leave', **kwargs)
    return _post_request(server_url=server_url,
                         resource_path=resource_path,
                         username=username,
                         password=password,
                         data=kwargs).json()


@docstring(server_url=SERVER_URL_DOC,
           username=USERNAME_DOC,
           password=PASSWORD_DOC,
           count=GROUP_COUNT,
           group_dict=GROUP_DICT)
def list_all(server_url: str,
             username: str='',
             password: str='',
             **kwargs) -> list:
    """List all local groups.

    :param server_url: {server_url}
    :param username: (optional) {username}
    :param password: (optional) {password}
    :param count: (optional) {count}
    :return: list of dicts with following sctructure:
        {group_dict}
    """
    return _get_request(server_url=server_url,
                        resource_path='statusnet/groups/list_all',
                        username=username,
                        password=password,
                        params=kwargs).json()


@docstring(server_url=SERVER_URL_DOC,
           username=USERNAME_DOC,
           password=PASSWORD_DOC,
           user_id=USER_ID_DOC,
           screen_name=SCREEN_NAME_DOC,
           count=GROUP_COUNT,
           group_dict=GROUP_DICT)
def user_groups(server_url: str,
                username: str='',
                password: str='',
                **kwargs) -> list:
    """Show the groups a given user is a member of.

    :param server_url: {server_url}
    :param username: (optional) {username}
    :param password: (optional) {password}
    :param user_id: (optional) {user_id}
    :param screen_name: (optional) {screen_name}
    :param count: (optional) {count}
    :return: list of dicts with following sctructure:
        {group_dict}
    """
    _check_user_target(username, **kwargs)
    return _post_request(server_url=server_url,
                         resource_path='statusnet/groups/list',
                         username=username,
                         password=password,
                         data=kwargs).json()


@docstring(server_url=SERVER_URL_DOC,
           username=USERNAME_DOC,
           password=PASSWORD_DOC,
           id=GROUP_ID_DOC,
           nickname=GROUP_NAME_DOC,
           count=USERS_COUNT,
           user_dict=USER_DICT)
def members(server_url: str,
            username: str='',
            password: str='',
            **kwargs) -> list:
    """List the members of a given group.

    :param server_url: {server_url}
    :param username: (optional) {username}
    :param password: (optional) {password}
    :param id: (optional) {id}
    :param nickname: (optional) {nickname}
    :param count: (optional) {count}
    :return: list of dicts with following sctructure:
        {user_dict}
    """
    resource_path = _resource_path('statusnet/groups/membership', **kwargs)
    return _post_request(server_url=server_url,
                         resource_path=resource_path,
                         username=username,
                         password=password,
                         data=kwargs).json()


@docstring(server_url=SERVER_URL_DOC,
           username=USERNAME_DOC,
           password=PASSWORD_DOC,
           user_id=USER_ID_DOC,
           screen_name=SCREEN_NAME_DOC,
           group_id=GROUP_ID_DOC,
           group_name=GROUP_NAME_DOC)
def is_member(server_url: str,
              username: str='',
              password: str='',
              **kwargs) -> dict:
    """Determine whether a given user is a member of a given group.

    :param server_url: {server_url}
    :param username: (optional) {username}
    :param password: (optional) {password}
    :param user_id: (optional) {user_id}
    :param screen_name: (optional) {screen_name}
    :param group_id: (optional) {group_id}
    :param group_name: (optional) {group_name}
    :return: a dict with following structure:
        is_member
    """
    _check_user_target(username, **kwargs)
    _check_group_id_and_name(**kwargs)
    return _post_request(server_url=server_url,
                         resource_path='statusnet/groups/is_member',
                         username=username,
                         password=password,
                         data=kwargs).json()


@docstring(server_url=SERVER_URL_DOC,
           username=USERNAME_DOC,
           password=PASSWORD_DOC,
           id=GROUP_ID_DOC,
           nickname=GROUP_NAME_DOC,
           count=USERS_COUNT,
           user_dict=USER_DICT)
def admins(server_url: str,
           username: str='',
           password: str='',
           **kwargs) -> list:
    """List the admins of a given group.

    :param server_url: {server_url}
    :param username: (optional) {username}
    :param password: (optional) {password}
    :param id: (optional) {id}
    :param nickname: (optional) {nickname}
    :param count: (optional) {count}
    :return: list of dicts with following sctructure:
        {user_dict}
    """
    resource_path = _resource_path('statusnet/groups/admins', **kwargs)
    return _get_request(server_url=server_url,
                        resource_path=resource_path,
                        username=username,
                        password=password,
                        params=kwargs).json()
