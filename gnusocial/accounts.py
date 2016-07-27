"""
gnusocial.accounts
~~~~~~~~~~~~~~~~~~

Module with account resources.
"""
from .utils import _get_request, _post_request, docstring
from .docs import (SERVER_URL_DOC, USERNAME_DOC, PASSWORD_DOC, LOCATION_DOC,
                   PROFILE_IMAGE_FILENAME_DOC, USER_DICT, NAME_DOC, URL_DOC,
                   DESCRIPTION_DOC, PROFILE_LINK_COLOR_DOC)


@docstring(server_url=SERVER_URL_DOC,
           username=USERNAME_DOC,
           password=PASSWORD_DOC)
def verify_credentials(server_url: str, username: str, password: str) -> None:
    """Tests if supplied user credentials are valid.
    If the credentials were valid, return None.
    If the credentials were invalid, raise gnusocial.utils.AuthenticationError.

    :param server_url: {server_url}
    :param username: {username}
    :param password: {password}
    """
    _get_request(
        server_url=server_url,
        resource_path='account/verify_credentials',
        username=username,
        password=password
    )


@docstring(server_url=SERVER_URL_DOC,
           username=USERNAME_DOC,
           password=PASSWORD_DOC,
           filename=PROFILE_IMAGE_FILENAME_DOC,
           user_dict=USER_DICT)
def update_profile_image(server_url: str,
                         username: str,
                         password: str,
                         filename: str) -> dict:
    """Updates the authenticating user's profile image.

    :param server_url: {server_url}
    :param username: {username}
    :param password: {password}
    :param filename: {filename}
    :return: dict with following structure:
        {user_dict}
    """
    image = {'image': open(filename, 'rb')}
    return _post_request(server_url=server_url,
                         resource_path='account/update_profile_image',
                         username=username,
                         password=password,
                         media=image).json()


@docstring(server_url=SERVER_URL_DOC,
           username=USERNAME_DOC,
           password=PASSWORD_DOC,
           name=NAME_DOC,
           url=URL_DOC,
           location=LOCATION_DOC,
           description=DESCRIPTION_DOC,
           profile_link_color=PROFILE_LINK_COLOR_DOC,
           user_dict=USER_DICT)
def update_profile(server_url: str,
                   username: str,
                   password: str,
                   **kwargs) -> dict:
    """Sets some values that users are able to set under the "Account" tab of
    their settings page. Only the parameters specified will be updated.

    :param server_url: {server_url}
    :param username: {username}
    :param password: {password}
    :param name: (optional) {name}
    :param url: (optional) {url}
    :param location: (optional) {location}
    :param description: (optional) {description}
    :param profile_link_color: (optional) {profile_link_color}
    :return: dict with following structure:
        {user_dict}
    """
    return _post_request(server_url=server_url,
                         resource_path='account/update_profile',
                         username=username,
                         password=password,
                         data=kwargs).json()
