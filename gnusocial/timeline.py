from functools import partial
from .utils import _get_request


def public(server_url: str, username: str='', password: str='') -> dict:
    get = partial(_get_request, server_url, 'statuses/public_timeline')
    if username:
        return get(credentials=(username, password))
    else:
        return get()


def home(server_url: str, username: str, password: str) -> dict:
    return _get_request(server_url,
                        'statuses/home_timeline',
                        (username, password))


def friends(server_url: str, username: str, password: str) -> dict:
    return _get_request(server_url,
                        'statuses/friends_timeline',
                        (username, password))


def user(server_url: str,
         target_user: str,
         username: str='',
         password: str='') -> dict:
    get = partial(_get_request,
                  server_url,
                  'statuses/friends_timeline/' + target_user)
    if username:
        return get(credentials=(username, password))
    else:
        return get()


def mentions(server_url: str, username: str, password: str) -> dict:
    return _get_request(server_url,
                        'statuses/mentions',
                        (username, password))


def replies(server_url: str,
            username: str='',
            password: str='',
            target_user: str='') -> dict:
    get = partial(_get_request,
                  server_url,
                  resource_path='statuses/replies/' + target_user)
    if username:
        return get(credentials=(username, password))
    elif not target_user:
        raise Exception(
            "You must either specify the user or supply the credentials."
        )
    else:
        return get()
