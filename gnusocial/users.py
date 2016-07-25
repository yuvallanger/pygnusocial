"""
gnusocial.users
~~~~~~~~~~~~~~~

Module with user resources.
"""
from .utils import _get_request, _check_user_target


def following(server_url: str,
              username: str='',
              password: str='',
              **kwargs) -> list:
    """Returns a collection of user objects for users followed by
    the specified user.

    :param server_url: URL of the server
    :param username: (optional) name of the authenticating user
    :param password: (optional) password of the authenticating user
    :param user_id: (optional) The ID of the user for whom to return results
        for.
    :param screen_name: (optional) The screen name of the user for whom to
        return results for.
    :param count: (optional) Specifies the number of users to try
        and retrieve.
    :return: a list of user info dicts
    """
    _check_user_target(username, **kwargs)
    return _get_request(server_url=server_url,
                        resource_path='statuses/friends',
                        username=username,
                        password=password,
                        params=kwargs).json()


def followers(server_url: str,
              username: str='',
              password: str='',
              **kwargs) -> list:
    """Returns a collection of user objects for users following
    the specified user.

    :param server_url: URL of the server
    :param username: (optional) name of the authenticating user
    :param password: (optional) password of the authenticating user
    :param user_id: (optional) The ID of the user for whom to return results
        for.
    :param screen_name: (optional) The screen name of the user for whom to
        return results for.
    :param count: (optional) Specifies the number of users to try
        and retrieve.
    :return: a list of user info dicts
    """
    _check_user_target(username, **kwargs)
    return _get_request(server_url=server_url,
                        resource_path='statuses/followers',
                        username=username,
                        password=password,
                        params=kwargs).json()


def show(server_url: str,
         username: str='',
         password: str='',
         **kwargs):
    """Returns a variety of information about the user specified by the
    required user_id or screen_name parameter. The author’s most recent
    status will be returned inline when possible.

    :param server_url: URL of the server
    :param username: (optional) name of the authenticating user
    :param password: (optional) password of the authenticating user
    :param user_id: (optional) The ID of the user for whom to return results
        for.
    :param screen_name: (optional) The screen name of the user for whom to
        return results for.
    :return: user info dict
    """
    _check_user_target(username, **kwargs)
    return _get_request(server_url=server_url,
                        resource_path='users/show',
                        username=username,
                        password=password,
                        params=kwargs).json()
