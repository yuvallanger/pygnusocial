"""
gnusocial.favorites
~~~~~~~~~~~~~~~~~~~

Module with favorite resources.
"""
from .utils import _post_request, _check_user_id_and_screen_name


def favorites(server_url: str,
              username: str,
              password: str,
              **kwargs) -> list:
    """Returns the 20 most recent notices favorited by the authenticating or
    specified user.

    :param server_url: URL of the server
    :param username: name of the authenticating user
    :param password: password of the authenticating user
    :param user_id: (optional) The ID of the user for whom to return results
        for.
    :param screen_name: (optional) The screen name of the user for whom to
        return results for.
    :param count: (optional) Specifies the number of direct messages to try
        and retrieve, up to a maximum of 200.
    :param since_id: (optional) Returns results with an ID greater than
        (that is, more recent than) the specified ID.
    :param max_id: (optional) Returns results with an ID less than
        (that is, older than) or equal to the specified ID.
    :param include_entities: (optional) The entities node will not be included
        when set to false.
    :return: list of dicts with following structure:
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
    _check_user_id_and_screen_name(**kwargs)
    return _post_request(server_url=server_url,
                         resource_path='favorites',
                         username=username,
                         password=password,
                         data=kwargs).json()


def create(server_url: str,
           username: str,
           password: str,
           status_id: int) -> dict:
    """Favorites the status specified in the ID parameter as the
    authenticating user. Returns the liked status when successful.

    :param server_url: URL of the server
    :param username: name of the authenticating user
    :param password: password of the authenticating user
    :param status_id: The numerical ID of the desired status.
    :param include_entities: (optional) The entities node will not be included
        when set to false.
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
    return _post_request(server_url=server_url,
                         resource_path='favorites/create/%d' % status_id,
                         username=username,
                         password=password).json()


def destroy(server_url: str,
            username: str,
            password: str,
            status_id: int) -> dict:
    """Unfavorites the status specified in the ID parameter as the
    authenticating user. Returns the unliked status when successful.

    :param server_url: URL of the server
    :param username: name of the authenticating user
    :param password: password of the authenticating user
    :param status_id: The numerical ID of the desired status.
    :param include_entities: (optional) The entities node will not be included
        when set to false.
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
    return _post_request(server_url=server_url,
                         resource_path='favorites/destroy/%d' % status_id,
                         username=username,
                         password=password).json()
