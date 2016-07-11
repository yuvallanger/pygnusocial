from .utils import _post_request, _get_request


def create(server_url: str,
           username: str,
           password: str,
           target_user: str) -> dict:
    return _post_request(server_url,
                         'friendships/create',
                         username,
                         password,
                         {'id': target_user})
