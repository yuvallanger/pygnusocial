from functools import partial
from .utils import _get_request


def public(server_url: str, username: str='', password: str='') -> dict:
    get = partial(_get_request,
                  server_url,
                  'statuses/public_timeline',
                  extension='.as')
    if username:
        return get(username=username, password=password)
    else:
        return get()


def home(server_url: str, username: str, password: str) -> dict:
    return _get_request(server_url,
                        'statuses/home_timeline',
                        username,
                        password,
                        extension='.as')


def friends(server_url: str, username: str, password: str) -> dict:
    return _get_request(server_url,
                        'statuses/friends_timeline',
                        username,
                        password,
                        extension='.as')


def user(server_url: str,
         target_user: str,
         username: str='',
         password: str='') -> dict:
    get = partial(_get_request,
                  server_url,
                  'statuses/user_timeline/' + target_user,
                  extension='.as')
    if username:
        return get(username=username, password=password)
    else:
        return get()


def mentions(server_url: str, username: str, password: str) -> dict:
    return _get_request(server_url,
                        'statuses/mentions',
                        username,
                        password,
                        extension='.as')


def replies(server_url: str,
            username: str='',
            password: str='',
            target_user: str='') -> dict:
    resource_path = 'statuses/replies'
    if target_user:
        resource_path += '/' + target_user
    get = partial(_get_request,
                  server_url=server_url,
                  resource_path=resource_path,
                  extension='.as')
    if username:
        return get(username=username, password=password)
    elif not target_user:
        raise Exception(
            "You must either specify the user or supply the credentials."
        )
    else:
        return get()
