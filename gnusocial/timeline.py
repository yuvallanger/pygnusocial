from .utils import _get_request


def public(server_url: str, username: str='', password: str='') -> dict:
    if username:
        return _get_request(server_url,
                            'statuses/public_timeline',
                            (username, password))
    else:
        return _get_request(server_url, 'statuses/public_timeline')


def home(server_url: str, username: str, password: str) -> dict:
    return _get_request(server_url,
                        'statuses/home_timeline',
                        (username, password))


def friends(server_url: str, username: str, password: str) -> dict:
    return _get_request(server_url,
                        'statuses/friends_timeline',
                        (username, password))
