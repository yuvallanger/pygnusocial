"""
gnusocial.friendships
~~~~~~~~~~~~~~~~~~~~

Module with friendship resources.
"""
from typing import Union
from .utils import _post_request, _check_user_id_and_screen_name


def create(server_url: str,
           username: str,
           password: str,
           **kwargs) -> dict:
    """Allows the authenticating users to follow the user specified in the
    user_id or screen_name parameter.

    :param server_url: URL of the server
    :param username: name of the authenticating user
    :param password: password of the authenticating user
    :param user_id: (optional) The ID of the user for whom to befriend.
    :param screen_name: (optional) The screen name of the user for whom to
        befriend.
    :param follow: (optional) Enable notifications for the target user.
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
    _check_user_id_and_screen_name(**kwargs)
    return _post_request(server_url=server_url,
                         resource_path='friendships/create',
                         username=username,
                         password=password,
                         data=kwargs).json()


def destroy(server_url: str,
            username: str,
            password: str,
            **kwargs) -> dict:
    """Allows the authenticating users to unfollow the user specified in the
    user_id or screen_name parameter.

    :param server_url: URL of the server
    :param username: name of the authenticating user
    :param password: password of the authenticating user
    :param user_id: (optional) The ID of the user for whom to unfollow.
    :param screen_name: (optional) The screen name of the user for whom to
        unfollow.
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
    return _post_request(server_url=server_url,
                         resource_path='friendships/destroy',
                         username=username,
                         password=password,
                         data=kwargs).json()


def exists(server_url: str,
           source_user: Union[str, int],
           target_user: Union[str, int],
           username: str='',
           password: str='') -> bool:
    """Shows if source_user follows target_user.

    :param server_url: URL of the server
    :param source_user: User that is following. Can be an ID or screen name.
    :param target_user: User that is followed. Can be an ID or screen name.
    :param username: (optional) name of the authenticating user
    :param password: (optional) password of the authenticating user
    :return: True if source_user follows target_user. False otherwise.
    """
    data = {'user_a': source_user, 'user_b': target_user}
    return _post_request(server_url=server_url,
                         resource_path='friendships/exists',
                         username=username,
                         password=password,
                         data=data).json()


def show(server_url: str,
         username: str='',
         password: str='',
         **kwargs) -> dict:
    """Returns detailed information about the relationship between two
    arbitrary users.

    :param server_url: URL of the server
    :param username: (optional) name of the authenticating user
    :param password: (optional) password of the authenticating user
    :param source_id: (optional) The user_id of the subject user.
    :param source_screen_name: (optional) The screen_name of the subject user.
    :param target_id: (optional) The user_id of the target user.
    :param target_screen_name: (optional) The screen_name of the target user.
    :return: dict with following structure:
        relationship - dict with following structure:
            source - dict with following structure:
                blocking - True if source user is blocking target user
                followed_by - True if source user is followed by target user
                following - True if source user is following target user
                id
                notifications_enabled - If notifications about target user
                    are enabled for source user
                screen_name
            target - same as source
    """
    has_target_id = 'target_id' in kwargs
    has_target_screen_name = 'target_screen_name' in kwargs
    if has_target_id == has_target_screen_name:
        raise Exception(
            "You must either specify target_id or target_screen_name."
        )
    has_source_id = 'source_id' in kwargs
    has_source_screen_name = 'source_screen_name' in kwargs
    if has_source_id and has_source_screen_name:
        raise Exception(
            "You must either specify source_id or source_screen_name."
        )
    if (not has_source_id and not has_target_screen_name) and not username:
        raise Exception(
            "You must either specify source_id or " +
            "source_screen_name or username")
    return _post_request(server_url=server_url,
                         resource_path='friendships/show',
                         username=username,
                         password=password,
                         data=kwargs).json()
