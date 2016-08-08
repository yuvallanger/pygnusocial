"""
gnusocial.direct_messages
~~~~~~~~~~~~~~~~~~~~~~~~~

Module with direct messages resources.
"""
from dtd import docstring
from .utils import _post_request, _check_user_target
from .docs import (_SERVER_URL_DOC, _USERNAME_DOC, _PASSWORD_DOC,
                   _SINCE_ID_DOC, _MAX_ID_DOC, _DM_COUNT, _DM_DICT,
                   _USER_ID_DOC, _SCREEN_NAME_DOC, _TEXT_DOC)


@docstring(server_url=_SERVER_URL_DOC,
           username=_USERNAME_DOC,
           password=_PASSWORD_DOC,
           since_id=_SINCE_ID_DOC,
           max_id=_MAX_ID_DOC,
           count=_DM_COUNT,
           dm_dict=_DM_DICT)
def received(server_url: str, username: str, password: str, **kwargs) -> list:
    """Returns the 20 most recent direct messages sent to the authenticating
user. Includes detailed information about the sender and recipient user.
You can request up to 200 direct messages per call, and only the most
recent 200 DMs will be available using this endpoint.

:param str server_url: {server_url}
:param str username: {username}
:param str password: {password}
:param int since_id: (optional) {since_id}
:param int max_id: (optional) {max_id}
:param int count: (optional) {count}
:rtype: list
:return: list of dicts with following structure:

::

    {dm_dict}
    """
    return _post_request(server_url=server_url,
                         resource_path='direct_messages',
                         username=username,
                         password=password,
                         data=kwargs).json()


@docstring(server_url=_SERVER_URL_DOC,
           username=_USERNAME_DOC,
           password=_PASSWORD_DOC,
           since_id=_SINCE_ID_DOC,
           max_id=_MAX_ID_DOC,
           count=_DM_COUNT,
           dm_dict=_DM_DICT)
def sent(server_url: str, username: str, password: str, **kwargs) -> list:
    """Returns the 20 most recent direct messages sent by the authenticating
user. Includes detailed information about the sender and recipient user.
You can request up to 200 direct messages per call, and only the most
recent 200 DMs will be available using this endpoint.

:param str server_url: {server_url}
:param str username: {username}
:param str password: {password}
:param int since_id: (optional) {since_id}
:param int max_id: (optional) {max_id}
:param int count: (optional) {count}
:rtype: list
:return: list of dicts with following structure:

::

    {dm_dict}
    """
    return _post_request(server_url=server_url,
                         resource_path='direct_messages/sent',
                         username=username,
                         password=password,
                         data=kwargs).json()


@docstring(server_url=_SERVER_URL_DOC,
           username=_USERNAME_DOC,
           password=_PASSWORD_DOC,
           user_id=_USER_ID_DOC,
           screen_name=_SCREEN_NAME_DOC,
           text=_TEXT_DOC,
           dm_dict=_DM_DICT)
def new(server_url: str,
        username: str,
        password: str,
        text: str,
        **kwargs) -> dict:
    """ Sends a new direct message to the specified user from
the authenticating user.

:param str server_url: {server_url}
:param str username: {username}
:param str password: {password}
:param str text: {text}
:param int user_id: (optional) {user_id}
:param str screen_name: (optional) {screen_name}
:rtype: dict
:return: dict with following structure:

::

    {dm_dict}
    """
    _check_user_target(**kwargs)
    kwargs['text'] = text
    return _post_request(server_url=server_url,
                         resource_path='direct_messages/new',
                         username=username,
                         password=password,
                         data=kwargs).json()
