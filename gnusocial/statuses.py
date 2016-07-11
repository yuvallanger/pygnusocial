from .utils import _post_request, _get_request


def update(server_url: str,
           username: str,
           password: str,
           status: str,
           **kwargs) -> dict:
    media = None
    if 'media' in kwargs:
        media = {'media': open(kwargs['media'], 'rb')}
    kwargs['status'] = status
    return _post_request(server_url=server_url,
                         resource_path='statuses/update',
                         username=username,
                         password=password,
                         data=kwargs,
                         media=media).json()


def show(server_url: str,
         notice_id: int,
         username: str='',
         password: str='') -> dict:
    return _get_request(server_url=server_url,
                        resource_path='statuses/show/%d' % notice_id,
                        username=username,
                        password=password).json()


def destroy(server_url: str,
            username: str,
            password: str,
            notice_id: int) -> dict:
    return _post_request(server_url=server_url,
                         resource_path='statuses/destroy/%d' % notice_id,
                         username=username,
                         password=password).json()


def repeat(server_url: str,
           username: str,
           password: str,
           notice_id: int) -> dict:
    return _post_request(server_url=server_url,
                         resource_path='statuses/retweet/%d' % notice_id,
                         username=username,
                         password=password).json()
