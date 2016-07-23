"""
gnusocial.statuses
~~~~~~~~~~~~~~~~~~

Module with status resources.
"""
from .utils import _post_request, _get_request


def update(server_url: str,
           username: str,
           password: str,
           status: str,
           **kwargs) -> dict:
    """Updates the authenticating user's current status.

    :param server_url: URL of the server
    :param username: name of the authenticating user
    :param password: password of the authenticating user
    :param status: The text of your status update.
    :param source: (optional) The name of application you update the status
        from.
    :param in_reply_to_status_id: (optional) The ID of an existing status that
        the update is in reply to.
    :param lat: (optional) The latitude of the location this status refers to.
        This parameter will be ignored unless it is inside the range -90.0 to
        +90.0 (North is positive) inclusive. It will also be ignored if there
        isn’t a corresponding long parameter.
    :param long: (optional) The longitude of the location this tweet refers to.
        The valid ranges for longitude is -180.0 to +180.0 (East is positive)
        inclusive. This parameter will be ignored if outside that range, if
        it is not a number or if there not a corresponding lat parameter.
    :param display_coordinates: (optional) Whether or not to put a pin on the
        exact coordinates a status has been sent from.
    :param place_id: (optional) an ID of the place.
    :param media: (optional) the name of the file to upload with the status.
    :return: dict with following structure:
        attachment - list of dicts with following structure:
            height
            id
            large_thumb_url
            mimetype
            oembed
            size - size of attacment in kilobytes
            thumb_url
            url
            version
            width
        attentions - list dicts with following structure:
            fullname
            id
            ostatus_uri
            profileurl
            screen_name
        created_at
        external_url
        fave_num - number of users favorited the notice
        favorited -  True if favorited by authenticated user
        geo
        id
        in_reply_to_ostatus_uri
        in_reply_to_profileurl
        in_reply_to_screen_name
        in_reply_to_status_id
        in_reply_to_user_id
        is_local
        is_post_verb
        repeat_num
        repeated - True if repeated by authenticated user
        repeated_id
        source
        statusnet_conversation_id
        statusnet_html - HTML contents of the notice
        statusnet_in_groups
        text - plain text contents of the notice
        truncated
        uri
        user - user info dict
    """
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
         status_id: int,
         username: str='',
         password: str='') -> dict:
    """Returns a single status, specified by the id parameter. The status'
        author will also be embedded within the status.

    :param server_url: URL of the server
    :param status_id: The numerical ID of the desired status.
    :param username: (optional) name of the authenticating user
    :param password: (optional) password of the authenticating user
    :return: status info dict
    """
    return _get_request(server_url=server_url,
                        resource_path='statuses/show/%d' % status_id,
                        username=username,
                        password=password).json()


def destroy(server_url: str,
            username: str,
            password: str,
            status_id: int) -> dict:
    """Destroys the status specified by the required ID parameter.
        The authenticating user must be the author of the specified status.
        Returns the destroyed status if successful.

    :param server_url: URL of the server
    :param username: name of the authenticating user
    :param password: password of the authenticating user
    :param status_id: The numerical ID of the desired status.
    :return: status info dict
    """
    return _post_request(server_url=server_url,
                         resource_path='statuses/destroy/%d' % status_id,
                         username=username,
                         password=password).json()


def repeat(server_url: str,
           username: str,
           password: str,
           status_id: int) -> dict:
    """Repeats a status. Returns the original status with repeat details
        embedded.

    :param server_url: URL of the server
    :param username: name of the authenticating user
    :param password: password of the authenticating user
    :param status_id: The numerical ID of the desired status.
    :return: status info dict
    """
    return _post_request(server_url=server_url,
                         resource_path='statuses/retweet/%d' % status_id,
                         username=username,
                         password=password).json()
