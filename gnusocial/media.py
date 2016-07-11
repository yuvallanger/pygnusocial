from .utils import _post_request


def upload(server_url: str,
           username: str,
           password: str,
           filename: str) -> str:
    media = {'media': open(filename, 'rb')}
    return _post_request(server_url=server_url,
                         resource_path='statusnet/media/upload',
                         extension='',
                         username=username,
                         password=password,
                         media=media).text()
