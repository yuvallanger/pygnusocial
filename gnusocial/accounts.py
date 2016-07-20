"""
gnusocial.accounts
~~~~~~~~~~~~~~~~~~

This module implements account resources.
"""
from .utils import _get_request, _post_request


def verify_credentials(server_url: str, username: str, password: str) -> None:
    """Tests if supplied user credentials are valid.
    If the credentials were valid, return None.
    If the credentials were invalid, raise gnusocial.utils.AuthenticationError.

    :param server_url: URL of the server
    :param username: name of the authenticating user
    :param password: password of the authenticating user
    """
    _get_request(
        server_url=server_url,
        resource_path='account/verify_credentials',
        username=username,
        password=password
    )


def update_profile_image(server_url: str,
                         username: str,
                         password: str,
                         filename: str) -> dict:
    """Updates the authenticating user's profile image.

    :param server_url: URL of the server
    :param username: name of the authenticating user
    :param password: password of the authenticating user
    :param filename: filename of the new profile picture
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
    image = {'image': open(filename, 'rb')}
    return _post_request(server_url=server_url,
                         resource_path='account/update_profile_image',
                         username=username,
                         password=password,
                         media=image).json()


def update_profile(server_url: str,
                   username: str,
                   password: str,
                   **kwargs) -> dict:
    """Sets some values that users are able to set under the "Account" tab of
    their settings page. Only the parameters specified will be updated.

    :param server_url: URL of the server
    :param username: name of the authenticating user
    :param password: password of the authenticating user
    :param name: (optional) full name associated with the profile
    :param url: (optional) URL associated with the profile.
        Will be prepended with "http://" if not present
    :param location: (optional) The city or country describing
        where the user of the account is located.
        The contents are not normalized or geocoded in any way
    :param description: (optional) A description of the user owning the account
    :param profile_link_color: (optional) Sets a hex value that controls the
        color scheme of links used on the authenticating user’s profile page.
        This must be a valid hexadecimal value,
        and may be either three or six characters (ex: F00 or FF0000).
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
        name
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
        url - user's URL or False if none
        utc_offset
    """
    return _post_request(server_url=server_url,
                         resource_path='account/update_profile',
                         username=username,
                         password=password,
                         data=kwargs).json()
