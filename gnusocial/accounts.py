from .utils import _get_request, _post_request


def verify_credentials(server_url: str, username: str, password: str) -> dict:
    _get_request(
        server_url=server_url,
        resource_path='account/verify_credentials',
        username=username,
        password=password
    )


def update_profile_image(server_url: str,
                         username: str,
                         password: str,
                         filename: str) -> dict:
    image = {'image': open(filename, 'rb')}
    return _post_request(server_url=server_url,
                         resource_path='account/update_profile_image',
                         username=username,
                         password=password,
                         media=image).json()


def update_profile(server_url: str,
                   username: str,
                   password: str,
                   **kwargs) -> dict:
    return _post_request(server_url=server_url,
                         resource_path='account/update_profile',
                         username=username,
                         password=password,
                         data=kwargs).json()
