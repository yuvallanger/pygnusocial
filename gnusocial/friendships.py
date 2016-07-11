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


def destroy(server_url: str,
            username: str,
            password: str,
            target_user: str) -> dict:
    return _post_request(server_url,
                         'friendships/destroy',
                         username,
                         password,
                         {'id': target_user})


def exists(server_url: str,
           user_a: str,
           user_b: str,
           username: str='',
           password: str='') -> dict:
    return _post_request(server_url=server_url,
                         resource_path='friendships/exists',
                         username=username,
                         password=password,
                         data={'user_a': user_a, 'user_b': user_b})
