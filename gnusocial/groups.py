"""
gnusocial.groups
~~~~~~~~~~~~~~~~

Module with group resources.
"""
from dtd import docstring
from .utils import (_post_request, _get_request, _check_id_and_nickname,
                    _check_user_target, _check_group_id_and_name)
from .docs import (_SERVER_URL_DOC, _USERNAME_DOC, _PASSWORD_DOC, _USER_DICT,
                   _USER_ID_DOC, _SCREEN_NAME_DOC, _GROUP_COUNT, _STATUS_DICT,
                   _GROUP_ID_DOC, _GROUP_NAME_DOC, _MAX_ID_DOC, _SINCE_ID_DOC,
                   _GROUP_DICT, _GROUP_DESCRIPTION, _GROUP_LOCATION,
                   _ALIASES_DOC, _HOMEPAGE_DOC, _FULLNAME_DOC, _USERS_COUNT)


def _resource_path(resource_path: str, **kwargs) -> str:
    _check_id_and_nickname(**kwargs)
    group_id = kwargs.get('id')
    group_name = kwargs.get('nickname')
    if group_id:
        resource_path += '/%d' % group_id
    if group_name:
        resource_path += '/%s' % group_name
    return resource_path


@docstring(server_url=_SERVER_URL_DOC,
           username=_USERNAME_DOC,
           password=_PASSWORD_DOC,
           id=_GROUP_ID_DOC,
           nickname=_GROUP_NAME_DOC,
           count=_GROUP_COUNT,
           since_id=_SINCE_ID_DOC,
           max_id=_MAX_ID_DOC,
           status_dict=_STATUS_DICT)
def timeline(server_url: str,
             username: str='',
             password: str='',
             **kwargs) -> list:
    """Shows a group's timeline. Similar to other timeline resources.

:param str server_url: {server_url}
:param str username: (optional) {username}
:param str password: (optional) {password}
:param int id: (optional) {id}
:param str nickname: (optional) {nickname}
:param int since_id: (optional) {since_id}
:param int max_id: (optional) {max_id}
:param int count: (optional) {count}
:rtype: list
:return: list of dicts with following sctructure:

::

    {status_dict}
    """
    resource_path = _resource_path('statusnet/groups/timeline', **kwargs)
    return _post_request(server_url=server_url,
                         resource_path=resource_path,
                         username=username,
                         password=password,
                         data=kwargs).json()


@docstring(server_url=_SERVER_URL_DOC,
           username=_USERNAME_DOC,
           password=_PASSWORD_DOC,
           id=_GROUP_ID_DOC,
           nickname=_GROUP_NAME_DOC,
           group_dict=_GROUP_DICT)
def show(server_url: str,
         username: str='',
         password: str='',
         **kwargs) -> dict:
    """Show a group's profile.

:param str server_url: {server_url}
:param str username: (optional) {username}
:param str password: (optional) {password}
:param int id: (optional) {id}
:param str nickname: (optional) {nickname}
:rtype: dict
:return: dict with following sctructure:

::

    {group_dict}
    """
    resource_path = _resource_path('statusnet/groups/show', **kwargs)
    return _get_request(server_url=server_url,
                        resource_path=resource_path,
                        username=username,
                        password=password,
                        params=kwargs).json()


@docstring(server_url=_SERVER_URL_DOC,
           username=_USERNAME_DOC,
           password=_PASSWORD_DOC,
           full_name=_FULLNAME_DOC,
           homepage=_HOMEPAGE_DOC,
           description=_GROUP_DESCRIPTION,
           location=_GROUP_LOCATION,
           aliases=_ALIASES_DOC,
           group_dict=_GROUP_DICT)
def create(server_url: str,
           username: str,
           password: str,
           **kwargs) -> dict:
    """Create a new group.

:param str server_url: {server_url}
:param str username: {username}
:param str password: {password}
:param str nickname: the name of the new group
:param str full_name: (optional) {full_name}
:param str homepage: (optional) {homepage}
:param str description: (optional) {description}
:param str location: (optional) {location}
:param aliases: (optional) {aliases}
:type aliases: list of strs
:rtype: dict
:return: dict with following sctructure:

::

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


@docstring(server_url=_SERVER_URL_DOC,
           username=_USERNAME_DOC,
           password=_PASSWORD_DOC,
           id=_GROUP_ID_DOC,
           nickname=_GROUP_NAME_DOC,
           group_dict=_GROUP_DICT)
def join(server_url: str,
         username: str,
         password: str,
         **kwargs) -> dict:
    """Join a group.

:param str server_url: {server_url}
:param str username: {username}
:param str password: {password}
:param int id: (optional) {id}
:param str nickname: (optional) {nickname}
:rtype: dict
:return: dict with following sctructure:

::

    {group_dict}
    """
    resource_path = _resource_path('statusnet/groups/join', **kwargs)
    return _post_request(server_url=server_url,
                         resource_path=resource_path,
                         username=username,
                         password=password,
                         data=kwargs).json()


@docstring(server_url=_SERVER_URL_DOC,
           username=_USERNAME_DOC,
           password=_PASSWORD_DOC,
           id=_GROUP_ID_DOC,
           nickname=_GROUP_NAME_DOC,
           group_dict=_GROUP_DICT)
def leave(server_url: str,
          username: str,
          password: str,
          **kwargs) -> dict:
    """Leave a group.

:param str server_url: {server_url}
:param str username: {username}
:param str password: {password}
:param int id: (optional) {id}
:param str nickname: (optional) {nickname}
:rtype: dict
:return: dict with following sctructure:

::

    {group_dict}
    """
    resource_path = _resource_path('statusnet/groups/leave', **kwargs)
    return _post_request(server_url=server_url,
                         resource_path=resource_path,
                         username=username,
                         password=password,
                         data=kwargs).json()


@docstring(server_url=_SERVER_URL_DOC,
           username=_USERNAME_DOC,
           password=_PASSWORD_DOC,
           count=_GROUP_COUNT,
           group_dict=_GROUP_DICT)
def list_all(server_url: str,
             username: str='',
             password: str='',
             **kwargs) -> list:
    """List all local groups.

:param str server_url: {server_url}
:param str username: (optional) {username}
:param str password: (optional) {password}
:param int count: (optional) {count}
:rtype: list
:return: list of dicts with following sctructure:

::

    {group_dict}
    """
    return _get_request(server_url=server_url,
                        resource_path='statusnet/groups/list_all',
                        username=username,
                        password=password,
                        params=kwargs).json()


@docstring(server_url=_SERVER_URL_DOC,
           username=_USERNAME_DOC,
           password=_PASSWORD_DOC,
           user_id=_USER_ID_DOC,
           screen_name=_SCREEN_NAME_DOC,
           count=_GROUP_COUNT,
           group_dict=_GROUP_DICT)
def user_groups(server_url: str,
                username: str='',
                password: str='',
                **kwargs) -> list:
    """Show the groups a given user is a member of.

:param str server_url: {server_url}
:param str username: (optional) {username}
:param str password: (optional) {password}
:param int user_id: (optional) {user_id}
:param str screen_name: (optional) {screen_name}
:param int count: (optional) {count}
:rtype: list
:return: list of dicts with following sctructure:

::

    {group_dict}
    """
    _check_user_target(username, **kwargs)
    return _post_request(server_url=server_url,
                         resource_path='statusnet/groups/list',
                         username=username,
                         password=password,
                         data=kwargs).json()


@docstring(server_url=_SERVER_URL_DOC,
           username=_USERNAME_DOC,
           password=_PASSWORD_DOC,
           id=_GROUP_ID_DOC,
           nickname=_GROUP_NAME_DOC,
           count=_USERS_COUNT,
           user_dict=_USER_DICT)
def members(server_url: str,
            username: str='',
            password: str='',
            **kwargs) -> list:
    """List the members of a given group.

:param str server_url: {server_url}
:param str username: (optional) {username}
:param str password: (optional) {password}
:param int id: (optional) {id}
:param str nickname: (optional) {nickname}
:param int count: (optional) {count}
:rtype: list
:return: list of dicts with following sctructure:

::

    {user_dict}
    """
    resource_path = _resource_path('statusnet/groups/membership', **kwargs)
    return _post_request(server_url=server_url,
                         resource_path=resource_path,
                         username=username,
                         password=password,
                         data=kwargs).json()


@docstring(server_url=_SERVER_URL_DOC,
           username=_USERNAME_DOC,
           password=_PASSWORD_DOC,
           user_id=_USER_ID_DOC,
           screen_name=_SCREEN_NAME_DOC,
           group_id=_GROUP_ID_DOC,
           group_name=_GROUP_NAME_DOC)
def is_member(server_url: str,
              username: str='',
              password: str='',
              **kwargs) -> dict:
    """Determine whether a given user is a member of a given group.

:param str server_url: {server_url}
:param str username: (optional) {username}
:param str password: (optional) {password}
:param int user_id: (optional) {user_id}
:param str screen_name: (optional) {screen_name}
:param int group_id: (optional) {group_id}
:param str group_name: (optional) {group_name}
:rtype: dict
:return: a dict with following structure:

::

    {{
        'is_member': bool
    }}
    """
    _check_user_target(username, **kwargs)
    _check_group_id_and_name(**kwargs)
    return _post_request(server_url=server_url,
                         resource_path='statusnet/groups/is_member',
                         username=username,
                         password=password,
                         data=kwargs).json()


@docstring(server_url=_SERVER_URL_DOC,
           username=_USERNAME_DOC,
           password=_PASSWORD_DOC,
           id=_GROUP_ID_DOC,
           nickname=_GROUP_NAME_DOC,
           count=_USERS_COUNT,
           user_dict=_USER_DICT)
def admins(server_url: str,
           username: str='',
           password: str='',
           **kwargs) -> list:
    """List the admins of a given group.

:param str server_url: {server_url}
:param str username: (optional) {username}
:param str password: (optional) {password}
:param int id: (optional) {id}
:param str nickname: (optional) {nickname}
:param int count: (optional) {count}
:rtype: list
:return: list of dicts with following sctructure:

::

    {user_dict}
    """
    resource_path = _resource_path('statusnet/groups/admins', **kwargs)
    return _get_request(server_url=server_url,
                        resource_path=resource_path,
                        username=username,
                        password=password,
                        params=kwargs).json()
