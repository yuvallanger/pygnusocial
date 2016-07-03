from .utils import _post_request


def update(server_url: str,
           username: str,
           password: str,
           status: str,
           source: str = '',
           in_reply_to_status_id: int = 0,
           latitude: int = -200,
           longitude: int = -200,
           place_id: str = '',
           display_coordinates: bool = False,
           ) -> dict:
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
