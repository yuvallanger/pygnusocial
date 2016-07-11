from .utils import _get_request, _post_request


def _check_args(**kwargs):
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
