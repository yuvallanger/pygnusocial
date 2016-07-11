from .utils import _post_request, _check_user_id_and_screen_name


def create(server_url: str,
           username: str,
           password: str,
           **kwargs) -> dict:
    _check_user_id_and_screen_name(**kwargs)
    return _post_request(server_url=server_url,
                         resource_path='blocks/create',
                         username=username,
                         password=password,
                         data=kwargs)


def destroy(server_url: str,
            username: str,
            password,
            **kwargs) -> dict:
    _check_user_id_and_screen_name(**kwargs)
    return _post_request(server_url=server_url,
                         resource_path='blocks/destroy',
                         username=username,
                         password=password,
                         data=kwargs)
