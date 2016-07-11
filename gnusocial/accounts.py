from .utils import _get_request


def verify_credentials(server_url: str, username: str, password: str) -> dict:
    _get_request(
        server_url=server_url,
        resource_path='account/verify_credentials',
        username=username,
        password=password
    )
