"""
gnusocial.blocks
~~~~~~~~~~~~~~~~

Module with block resources.
"""
from dtd import docstring
from .utils import _post_request, _check_user_target
from .docs import (_SERVER_URL_DOC, _USERNAME_DOC, _PASSWORD_DOC, _USER_DICT,
                   _USER_ID_DOC, _SCREEN_NAME_DOC)


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
    """Blocks the specified user from following the authenticating user.
In addition the blocked user will not show in the authenticating users
mentions or timeline (unless repeated by another user). If a follow or
friend relationship exists it is destroyed.

:param str server_url: {server_url}
:param str username: {username}
:param str password: {password}
:param int user_id: (optional) {user_id}
:param str screen_name: (optional) {screen_name}
:rtype: dict
:return: dict with following structure:

::

    {user_dict}
    """
    _check_user_target(**kwargs)
    return _post_request(server_url=server_url,
                         resource_path='blocks/create',
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
    """Un-blocks the specified user from following the authenticating user.
If relationships existed before the block was instated,
they will not be restored.

:param str server_url: {server_url}
:param str username: {username}
:param str password: {password}
:param int user_id: (optional) {user_id}
:param str screen_name: (optional) {screen_name}
:rtype: dict
:return: dict with following structure:

::

    {user_dict}
    """
    _check_user_target(**kwargs)
    return _post_request(server_url=server_url,
                         resource_path='blocks/destroy',
                         username=username,
                         password=password,
                         data=kwargs).json()
