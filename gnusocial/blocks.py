"""
gnusocial.blocks
~~~~~~~~~~~~~~~~

Module with block resources.
"""
from .utils import _post_request, _check_user_target


def create(server_url: str,
           username: str,
           password: str,
           **kwargs) -> dict:
    """Blocks the specified user from following the authenticating user.
    In addition the blocked user will not show in the authenticating users
    mentions or timeline (unless repeated by another user). If a follow or
    friend relationship exists it is destroyed.

    :param server_url: URL of the server
    :param username: name of the authenticating user
    :param password: password of the authenticating user
    :param screen_name: (optional) The screen name of the potentially blocked
        user.
    :param user_id: (optional) The ID of the potentially blocked user.
    :param include_entities: (optional) The entities node will not be included
        when set to false.
    :param skip_status: (optional) When set to either True or 1 statuses
        will not be included in the returned user objects.
    :return: dict with following structure:
        background_image - URL to background image or False if none
        backgroundcolor - background color in hex or False if default
        cover_photo - URL to cover image or False if none
        created_at - the date of user registration
        description - user profile description or False if none
        favourites_count - the number of notices favorited by user
        followers_count
        following - True if authenticating user is following the user
        friends_count - the number of users user is following
        groups_count - the number of group user is member of
        id
        is_local - True if user is from server_url
        is_sandboxed
        is_silenced
        linkcolor - link color in hex or False if default
        location - user's location or False if none
        name - full name associated with the profile
        notifications - True if authenticating user
            is getting notifications from user
        ostatus_uri - URL to user profile
        profile_background_color - same as backgroundcolor
        profile_banner_url - same as cover_photo
        profile_image_url - URL to 48x48 avatar image
        profile_image_url_https - same as profile_image_url, but with HTTPS
        profile_image_url_original - URL to avatar image in original resolution
        profile_image_url_profile_size - URL to 96x96 avatar image
        profile_link_color - same as linkcolor
        protected
        rights - a dict of what user can do:
            delete_others_notice
            delete_user
            sandbox
            silence
        screen_name - user's handle
        status - user's latest status
        statuses_count
        statusnet_blocking
        statusnet_profile_url
        time_zone
        url - URL associated with the profile or False if none
        utc_offset
    """
    _check_user_target(**kwargs)
    return _post_request(server_url=server_url,
                         resource_path='blocks/create',
                         username=username,
                         password=password,
                         data=kwargs).json()


def destroy(server_url: str,
            username: str,
            password: str,
            **kwargs) -> dict:
    """Un-blocks the specified user from following the authenticating user.
     If relationships existed before the block was instated,
     they will not be restored.

    :param server_url: URL of the server
    :param username: name of the authenticating user
    :param password: password of the authenticating user
    :param screen_name: (optional) The screen name of the potentially blocked
        user.
    :param user_id: (optional) The ID of the potentially blocked user.
    :param include_entities: (optional) The entities node will not be included
        when set to false.
    :param skip_status: (optional) When set to either True or 1 statuses
        will not be included in the returned user objects.
    :return: dict with following structure:
        background_image - URL to background image or False if none
        backgroundcolor - background color in hex or False if default
        cover_photo - URL to cover image or False if none
        created_at - the date of user registration
        description - user profile description or False if none
        favourites_count - the number of notices favorited by user
        followers_count
        following - True if authenticating user is following the user
        friends_count - the number of users user is following
        groups_count - the number of group user is member of
        id
        is_local - True if user is from server_url
        is_sandboxed
        is_silenced
        linkcolor - link color in hex or False if default
        location - user's location or False if none
        name - full name associated with the profile
        notifications - True if authenticating user
            is getting notifications from user
        ostatus_uri - URL to user profile
        profile_background_color - same as backgroundcolor
        profile_banner_url - same as cover_photo
        profile_image_url - URL to 48x48 avatar image
        profile_image_url_https - same as profile_image_url, but with HTTPS
        profile_image_url_original - URL to avatar image in original resolution
        profile_image_url_profile_size - URL to 96x96 avatar image
        profile_link_color - same as linkcolor
        protected
        rights - a dict of what user can do:
            delete_others_notice
            delete_user
            sandbox
            silence
        screen_name - user's handle
        status - user's latest status
        statuses_count
        statusnet_blocking
        statusnet_profile_url
        time_zone
        url - URL associated with the profile or False if none
        utc_offset
    """
    _check_user_target(**kwargs)
    return _post_request(server_url=server_url,
                         resource_path='blocks/destroy',
                         username=username,
                         password=password,
                         data=kwargs).json()
