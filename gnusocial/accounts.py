"""
gnusocial.accounts
~~~~~~~~~~~~~~~~~~

Module with account resources.
"""
from dtd import docstring
from .utils import _get_request, _post_request
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

:param str server_url: {server_url}
:param str username: {username}
:param str password: {password}
:raises gnusocial.utils.AuthenticationError: if credentials are invalid
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

:param str server_url: {server_url}
:param str username: {username}
:param str password: {password}
:param str filename: filename of the new profile picture
:rtype: dict
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

:param str server_url: {server_url}
:param str username: {username}
:param str password: {password}
:param str name: (optional) {name}
:param str url: (optional) {url}
:param str location: (optional) {location}
:param str description: (optional) {description}
:param str profile_link_color: (optional) {profile_link_color}
:rtype: dict
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

:param str server_url: {server_url}
:param str nickname: name of the new user
:param str password: desired password
:param str confirm: password confirmation
:param str email: (optional) email associated with the new user
:param str fullname: (optional) {fullname}
:param str homepage: (optional) {homepage}
:param str location: (optional) {location}
:param str bio: (optional) {bio}
:rtype dict:
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
