from .utils import _get_request, _post_request


def received(server_url: str, username: str, password: str) -> list:
    return _get_request(server_url, 'direct_messages', username, password)


def sent(server_url: str, username: str, password: str) -> list:
    return _get_request(server_url, 'direct_messages/sent', username, password)


def new(server_url: str,
        username: str,
        password: str,
        target_user: str,
        text: str) -> list:
    data = {'user': target_user, 'text': text}
    return _post_request(server_url=server_url,
                         resource_path='direct_messages/new',
                         username=username,
                         password=password,
                         data=data)
