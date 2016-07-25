"""
gnusocial.direct_messages
~~~~~~~~~~~~~~~~~~~~~~~~~

Module with direct messages resources.
"""
from .utils import _get_request, _post_request, _check_user_target


def received(server_url: str, username: str, password: str, **kwargs) -> list:
    """Returns the 20 most recent direct messages sent to the authenticating
    user. Includes detailed information about the sender and recipient user.
    You can request up to 200 direct messages per call, and only the most
    recent 200 DMs will be available using this endpoint.

    :param server_url: URL of the server
    :param username: name of the authenticating user
    :param password: password of the authenticating user
    :param since_id: (optional) Returns results with an ID greater than
        (that is, more recent than) the specified ID.
    :param max_id: (optional) Returns results with an ID less than
        (that is, older than) or equal to the specified ID.
    :param count: (optional) Specifies the number of direct messages to try
        and retrieve, up to a maximum of 200.
    :param include_entities: (optional) The entities node will not be included
        when set to false.
    :param skip_status: (optional) When set to either True or 1 statuses
        will not be included in the returned user objects.
    :return: list of dicts with following structure:
        created_at - date of message creation
        id
        recipient - user info dict
        recipient_id
        recipient_screen_name
        sender - user info dict
        sender_id
        sender_screen_name
        text
    """
    return _get_request(server_url=server_url,
                        resource_path='direct_messages',
                        username=username,
                        password=password,
                        params=kwargs).json()


def sent(server_url: str, username: str, password: str, **kwargs) -> list:
    """Returns the 20 most recent direct messages sent by the authenticating
    user. Includes detailed information about the sender and recipient user.
    You can request up to 200 direct messages per call, and only the most
    recent 200 DMs will be available using this endpoint.

    :param server_url: URL of the server
    :param username: name of the authenticating user
    :param password: password of the authenticating user
    :param since_id: (optional) Returns results with an ID greater than
        (that is, more recent than) the specified ID.
    :param max_id: (optional) Returns results with an ID less than
        (that is, older than) or equal to the specified ID.
    :param count: (optional) Specifies the number of direct messages to try
        and retrieve, up to a maximum of 200.
    :param include_entities: (optional) The entities node will not be included
        when set to false.
    :param skip_status: (optional) When set to either True or 1 statuses
        will not be included in the returned user objects.
    :return: list of dicts with following structure:
        created_at - date of message creation
        id
        recipient - user info dict
        recipient_id
        recipient_screen_name
        sender - user info dict
        sender_id
        sender_screen_name
        text
    """
    return _get_request(server_url=server_url,
                        resource_path='direct_messages/sent',
                        username=username,
                        password=password,
                        params=kwargs).json()


def new(server_url: str,
        username: str,
        password: str,
        text: str,
        **kwargs) -> dict:
    """ Sends a new direct message to the specified user from
    the authenticating user.

    :param server_url: URL of the server
    :param username: name of the authenticating user
    :param password: password of the authenticating user
    :param text: The text of your direct message.
    :param user_id: (optional) The ID of the user who should receive the
        direct message.
    :param screen_name: (optional) The screen name of the user who should
        receive the direct message.
    :return: dict with following structure:
        created_at - date of message creation
        id
        recipient - user info dict
        recipient_id
        recipient_screen_name
        sender - user info dict
        sender_id
        sender_screen_name
        text
    """
    _check_user_target(**kwargs)
    kwargs['text'] = text
    return _post_request(server_url=server_url,
                         resource_path='direct_messages/new',
                         username=username,
                         password=password,
                         data=kwargs).json()
