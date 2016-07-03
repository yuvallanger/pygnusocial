from .utils import _get_request


def public_timeline(server_url: str,
                    username: str = '',
                    password: str = '') -> list:
    if username:
        return _get_request(server_url,
                            'statuses/public_timeline',
                            (username, password))
    else:
        return _get_request(server_url, 'statuses/public_timeline')


def home_timeline(server_url: str, username: str, password: str) -> list:
    return _get_request(server_url,
                        'statuses/home_timeline',
                        (username, password))
