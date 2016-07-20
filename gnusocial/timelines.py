from .utils import _get_request


def public(server_url: str, username: str='', password: str='') -> dict:
    return _get_request(server_url=server_url,
                        resource_path='statuses/public_timeline',
                        extension='.as',
                        username=username,
                        password=password).json()


def home(server_url: str, username: str, password: str) -> dict:
    return _get_request(server_url=server_url,
                        resource_path='statuses/home_timeline',
                        username=username,
                        password=password,
                        extension='.as').json()


def friends(server_url: str, username: str, password: str) -> dict:
    return _get_request(server_url=server_url,
                        resource_path='statuses/friends_timeline',
                        username=username,
                        password=password,
                        extension='.as').json()


def user(server_url: str,
         target_user: str,
         username: str='',
         password: str='') -> dict:
    return _get_request(server_url=server_url,
                        resource_path='statuses/user_timeline/' + target_user,
                        extension='.as',
                        username=username,
                        password=password).json()


def mentions(server_url: str, username: str, password: str) -> dict:
    return _get_request(server_url=server_url,
                        resource_path='statuses/mentions',
                        username=username,
                        password=password,
                        extension='.as').json()


def replies(server_url: str,
            username: str='',
            password: str='',
            target_user: str='') -> dict:
    resource_path = 'statuses/replies'
    if target_user:
        resource_path += '/' + target_user
    if not target_user and not username:
        raise Exception(
            "You must either specify the user or supply the credentials."
        )
    return _get_request(server_url=server_url,
                        resource_path=resource_path,
                        extension='.as',
                        username=username,
                        password=password).json()
