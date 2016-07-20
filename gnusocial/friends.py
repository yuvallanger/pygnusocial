"""
gnusocial.friends
~~~~~~~~~~~~~~~~~

Module with friends resources.
"""
from typing import List
from .utils import _post_request


def _check_args(username: str='', **kwargs) -> None:
    both_targets = 'user_id' in kwargs and 'screen_name' in kwargs
    no_targets = 'user_id' not in kwargs and 'screen_name' not in kwargs
    if both_targets:
        raise Exception(
            "You must either specify the user_id or screen_name."
        )
    if no_targets and not username:
        raise Exception(
            "You must either specify the user_id or screen_name or " +
            "username."
        )


def friends(server_url: str,
            username: str='',
            password: str='',
            **kwargs) -> List[int]:
    """Returns IDs of users the auntenticated or
    specified user is following (otherwise known as their "friends").

    :param server_url: URL of the server
    :param username: (optional) name of the authenticating user
    :param password: (optional) password of the authenticating user
    :param user_id: (optional) The ID of the user for whom to return results
        for.
    :param screen_name: (optional) The screen name of the user for whom to
        return results for.
    :param count: (optional) Specifies the number of direct messages to try
        and retrieve, up to a maximum of 200.
    :param since_id: (optional) Returns results with an ID greater than
        (that is, more recent than) the specified ID.
    :param max_id: (optional) Returns results with an ID less than
        (that is, older than) or equal to the specified ID.
    :param include_entities: (optional) The entities node will not be included
        when set to false.
    :return: a list of user IDs
    """
    _check_args(username, **kwargs)
    return _post_request(server_url=server_url,
                         resource_path='friends/ids',
                         username=username,
                         password=password,
                         data=kwargs).json()


def followers(server_url: str,
              username: str='',
              password: str='',
              **kwargs) -> List[int]:
    """Returns IDs of users the auntenticated or
    specified user is followed by (otherwise known as their "friends").

    :param server_url: URL of the server
    :param username: (optional) name of the authenticating user
    :param password: (optional) password of the authenticating user
    :param user_id: (optional) The ID of the user for whom to return results
        for.
    :param screen_name: (optional) The screen name of the user for whom to
        return results for.
    :param count: (optional) Specifies the number of direct messages to try
        and retrieve, up to a maximum of 200.
    :param since_id: (optional) Returns results with an ID greater than
        (that is, more recent than) the specified ID.
    :param max_id: (optional) Returns results with an ID less than
        (that is, older than) or equal to the specified ID.
    :param include_entities: (optional) The entities node will not be included
        when set to false.
    :return: a list of user IDs
    """
    _check_args(username, **kwargs)
    return _post_request(server_url=server_url,
                         resource_path='followers/ids',
                         username=username,
                         password=password,
                         data=kwargs).json()
