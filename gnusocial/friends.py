from .utils import _post_request


def friends(server_url: str,
            username: str='',
            password: str='',
            **kwargs) -> list:
    both_targets = 'user_id' in kwargs and 'screen_name' in kwargs
    no_targets = 'user_id' not in kwargs and 'screen_name' not in kwargs
    if both_targets:
        raise Exception(
            "You must either specify the user_id or screen_name."
        )
    if no_targets and not username:
        raise Exception(
            "You must either specify the user_id or screen_name or " +
            "username."
        )
    return _post_request(server_url=server_url,
                         resource_path='friends/ids',
                         username=username,
                         password=password,
                         data=kwargs)
