from functools import partial
from .utils import _post_request, _get_request


def update(server_url: str,
           username: str,
           password: str,
           status: str,
           source: str='',
           in_reply_to_status_id: int=0,
           latitude: int=-200,
           longitude: int=-200,
           place_id: str='',
           display_coordinates: bool=False) -> dict:
    data = {
        'status': status,
        'source': source,
        'in_reply_to_status_id': in_reply_to_status_id,
        'latitude': latitude,
        'longitude': longitude,
        'place_id': place_id,
        'display_coordinates': str(display_coordinates).lower(),
    }
    return _post_request(server_url,
                         'statuses/update',
                         username,
                         password,
                         data)


def show(server_url: str,
         notice_id: int,
         username: str='',
         password: str='') -> dict:
    get = partial(_get_request,
                  server_url,
                  'statuses/show/%d' % notice_id,
                  extension='.json')
    if username:
        return get(username=username, password=password)
    return get()


def destroy(server_url: str,
            notice_id: int,
            username: str,
            password: str) -> dict:
    return _post_request(server_url,
                         'statuses/destroy/%d' % notice_id,
                         username,
                         password,
                         data=None)
