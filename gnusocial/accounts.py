"""
gnusocial.accounts
~~~~~~~~~~~~~~~~~~

Module with account resources.
"""
from .utils import _get_request, _post_request, docstring
from .docs import (_SERVER_URL_DOC, _USERNAME_DOC, _PASSWORD_DOC,
                   _USER_LOCATION, _USER_DICT, _NAME_DOC, _URL_DOC,
                   _USER_DESCRIPTION, _PROFILE_LINK_COLOR_DOC)


@docstring(server_url=_SERVER_URL_DOC,
           username=_USERNAME_DOC,
           password=_PASSWORD_DOC)
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


@docstring(server_url=_SERVER_URL_DOC,
           username=_USERNAME_DOC,
           password=_PASSWORD_DOC,
           user_dict=_USER_DICT)
def update_profile_image(server_url: str,
                         username: str,
                         password: str,
                         filename: str) -> dict:
    """Updates the authenticating user's profile image.

:param server_url: {server_url}
:param username: {username}
:param password: {password}
:param filename: filename of the new profile picture
:return: dict with following structure:

::

    {user_dict}
    """
    image = {'image': open(filename, 'rb')}
    return _post_request(server_url=server_url,
                         resource_path='account/update_profile_image',
                         username=username,
                         password=password,
                         media=image).json()


@docstring(server_url=_SERVER_URL_DOC,
           username=_USERNAME_DOC,
           password=_PASSWORD_DOC,
           name=_NAME_DOC,
           url=_URL_DOC,
           location=_USER_LOCATION,
           description=_USER_DESCRIPTION,
           profile_link_color=_PROFILE_LINK_COLOR_DOC,
           user_dict=_USER_DICT)
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

::

    {user_dict}
    """
    return _post_request(server_url=server_url,
                         resource_path='account/update_profile',
                         username=username,
                         password=password,
                         data=kwargs).json()


@docstring(server_url=_SERVER_URL_DOC,
           fullname=_NAME_DOC,
           homepage=_URL_DOC,
           location=_USER_LOCATION,
           bio=_USER_DESCRIPTION,
           user_dict=_USER_DICT)
def register(server_url: str,
             nickname: str,
             password: str,
             confirm: str,
             **kwargs) -> dict:
    """Registers a new user.

:param server_url: {server_url}
:param nickname: name of the new user
:param password: desired password
:param confirm: password confirmation
:param email: (optional) email associated with the new user
:param fullname: (optional) {fullname}
:param homepage: (optional) {homepage}
:param location: (optional) {location}
:param bio: (optional) {bio}
:return: dict with following structure:

::

    {user_dict}
    """
    kwargs['nickname'] = nickname
    kwargs['password'] = password
    kwargs['confirm'] = confirm
    return _post_request(server_url=server_url,
                         resource_path='account/register',
                         data=kwargs).json()
