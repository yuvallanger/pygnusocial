from .utils import _post_request


def _check_args(**kwargs) -> None:
    both_targets = 'user_id' in kwargs and 'screen_name' in kwargs
    if both_targets:
        raise Exception(
            "You must either specify the user_id or screen_name."
        )


def favorites(server_url: str,
              username: str,
              password: str,
              **kwargs) -> list:
    _check_args(**kwargs)
    return _post_request(server_url=server_url,
                         resource_path='favorites',
                         username=username,
                         password=password,
                         data=kwargs)


def create(server_url: str,
           username: str,
           password: str,
           post_id: int) -> dict:
    return _post_request(server_url=server_url,
                         resource_path='favorites/create/%d' % post_id,
                         username=username,
                         password=password)
