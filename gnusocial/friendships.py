from .utils import _post_request


def create(server_url: str,
           username: str,
           password: str,
           target_user: str) -> dict:
    return _post_request(server_url=server_url,
                         resource_path='friendships/create',
                         username=username,
                         password=password,
                         data={'id': target_user})


def destroy(server_url: str,
            username: str,
            password: str,
            target_user: str) -> dict:
    return _post_request(server_url=server_url,
                         resource_path='friendships/destroy',
                         username=username,
                         password=password,
                         data={'id': target_user})


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


def show(server_url: str,
         username: str='',
         password: str='',
         **kwargs) -> dict:
    both_targets = 'target_id' in kwargs and 'target_screen_name' in kwargs
    no_targets = 'target_id' not in kwargs and \
        'target_screen_name' not in kwargs
    if both_targets or no_targets:
        raise Exception(
            "You must either specify target_id or target_screen_name."
        )
    both_sources = 'source_id' in kwargs and 'source_screen_name' in kwargs
    no_sources = 'source_id' not in kwargs and \
        'source_screen_name' not in kwargs
    if both_sources:
        raise Exception(
            "You must either specify source_id or source_screen_name."
        )
    if no_sources and not username:
        raise Exception(
            "You must either specify source_id or " +
            "source_screen_name or username")
    return _post_request(server_url=server_url,
                         resource_path='friendships/show',
                         username=username,
                         password=password,
                         data=kwargs)
