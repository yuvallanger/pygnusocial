from .utils import _get_request


def following(server_url: str,
              username: str,
              password: str) -> list:
    return _get_request(server_url=server_url,
                        resource_path='statuses/friends',
                        username=username,
                        password=password).json()


def followers(server_url: str,
              username: str,
              password: str) -> list:
    return _get_request(server_url=server_url,
                        resource_path='statuses/followers',
                        username=username,
                        password=password).json()


def show(server_url: str,
         target_user: str,
         username: str='',
         password: str=''):
    return _get_request(server_url=server_url,
                        resource_path='users/show/' + target_user,
                        username=username,
                        password=password).json()
