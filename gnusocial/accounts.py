from .utils import _get_request, _post_request


def verify_credentials(server_url: str, username: str, password: str) -> dict:
    return _get_request(
        server_url=server_url,
        resource_path='account/verify_credentials',
        username=username,
        password=password
    ).json()


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
