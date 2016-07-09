from .utils import _get_request


def following(server_url: str,
              username: str,
              password: str) -> list:
    return _get_request(server_url,
                        'statuses/friends',
                        username,
                        password,
                        extension='.json')


def followers(server_url: str,
              username: str,
              password: str) -> list:
    return _get_request(server_url,
                        'statuses/followers',
                        username,
                        password,
                        extension='.json')
