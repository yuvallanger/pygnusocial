"""
gnusocial.direct_messages
~~~~~~~~~~~~~~~~~~~~~~~~~

Module with direct messages resources.
"""
from .utils import _post_request, _check_user_target, docstring
from .docs import (SERVER_URL_DOC, USERNAME_DOC, PASSWORD_DOC, SINCE_ID_DOC,
                   MAX_ID_DOC, DM_COUNT, DM_DICT, USER_ID_DOC, SCREEN_NAME_DOC,
                   TEXT_DOC)


@docstring(server_url=SERVER_URL_DOC,
           username=USERNAME_DOC,
           password=PASSWORD_DOC,
           since_id=SINCE_ID_DOC,
           max_id=MAX_ID_DOC,
           count=DM_COUNT,
           dm_dict=DM_DICT)
def received(server_url: str, username: str, password: str, **kwargs) -> list:
    """Returns the 20 most recent direct messages sent to the authenticating
    user. Includes detailed information about the sender and recipient user.
    You can request up to 200 direct messages per call, and only the most
    recent 200 DMs will be available using this endpoint.

    :param server_url: {server_url}
    :param username: {username}
    :param password: {password}
    :param since_id: (optional) {since_id}
    :param max_id: (optional) {max_id}
    :param count: (optional) {count}
    :return: list of dicts with following structure:
       {dm_dict}
    """
    return _post_request(server_url=server_url,
                         resource_path='direct_messages',
                         username=username,
                         password=password,
                         data=kwargs).json()


@docstring(server_url=SERVER_URL_DOC,
           username=USERNAME_DOC,
           password=PASSWORD_DOC,
           since_id=SINCE_ID_DOC,
           max_id=MAX_ID_DOC,
           count=DM_COUNT,
           dm_dict=DM_DICT)
def sent(server_url: str, username: str, password: str, **kwargs) -> list:
    """Returns the 20 most recent direct messages sent by the authenticating
    user. Includes detailed information about the sender and recipient user.
    You can request up to 200 direct messages per call, and only the most
    recent 200 DMs will be available using this endpoint.

    :param server_url: {server_url}
    :param username: {username}
    :param password: {password}
    :param since_id: (optional) {since_id}
    :param max_id: (optional) {max_id}
    :param count: (optional) {count}
    :return: list of dicts with following structure:
       {dm_dict}
    """
    return _post_request(server_url=server_url,
                         resource_path='direct_messages/sent',
                         username=username,
                         password=password,
                         data=kwargs).json()


@docstring(server_url=SERVER_URL_DOC,
           username=USERNAME_DOC,
           password=PASSWORD_DOC,
           user_id=USER_ID_DOC,
           screen_name=SCREEN_NAME_DOC,
           text=TEXT_DOC,
           dm_dict=DM_DICT)
def new(server_url: str,
        username: str,
        password: str,
        text: str,
        **kwargs) -> dict:
    """ Sends a new direct message to the specified user from
    the authenticating user.

    :param server_url: {server_url}
    :param username: {username}
    :param password: {password}
    :param text: {text}
    :param user_id: (optional) {user_id}
    :param screen_name: (optional) {screen_name}
    :return: dict with following structure:
        {dm_dict}
    """
    _check_user_target(**kwargs)
    kwargs['text'] = text
    return _post_request(server_url=server_url,
                         resource_path='direct_messages/new',
                         username=username,
                         password=password,
                         data=kwargs).json()
