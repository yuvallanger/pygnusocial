from .utils import _post_request, _check_user_id_and_screen_name


def favorites(server_url: str,
              username: str,
              password: str,
              **kwargs) -> list:
    _check_user_id_and_screen_name(**kwargs)
    return _post_request(server_url=server_url,
                         resource_path='favorites',
                         username=username,
                         password=password,
                         data=kwargs).json()


def create(server_url: str,
           username: str,
           password: str,
           post_id: int) -> dict:
    return _post_request(server_url=server_url,
                         resource_path='favorites/create/%d' % post_id,
                         username=username,
                         password=password).json()


def destroy(server_url: str,
            username: str,
            password: str,
            post_id: int) -> dict:
    return _post_request(server_url=server_url,
                         resource_path='favorites/destroy/%d' % post_id,
                         username=username,
                         password=password).json()
