from functools import partial
from .utils import _get_request


def following(server_url: str,
              username: str,
              password: str) -> list:
    return _get_request(server_url,
                        'statuses/friends',
                        username,
                        password)


def followers(server_url: str,
              username: str,
              password: str) -> list:
    return _get_request(server_url,
                        'statuses/followers',
                        username,
                        password)


def show(server_url: str,
         target_user: str,
         username: str='',
         password: str=''):
    get = partial(_get_request,
                  server_url,
                  'users/show/' + target_user)
    if username:
        return get(username=username, password=password)
    else:
        return get()
