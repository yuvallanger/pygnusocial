"""
gnusocial.statuses
~~~~~~~~~~~~~~~~~~

Module with status resources.
"""
from dtd import docstring
from .utils import _post_request, _get_request
from .docs import (_SERVER_URL_DOC, _USERNAME_DOC, _PASSWORD_DOC, _STATUS_DICT,
                   _STATUS_ID_DOC, _STATUSES_COUNT, _SINCE_ID_DOC, _MAX_ID_DOC)


@docstring(server_url=_SERVER_URL_DOC,
           username=_USERNAME_DOC,
           password=_PASSWORD_DOC,
           status_dict=_STATUS_DICT)
def update(server_url: str,
           username: str,
           password: str,
           status: str,
           **kwargs) -> dict:
    """Updates the authenticating user's current status.

:param str server_url: {server_url}
:param str username: {username}
:param str password: {password}
:param str status: The text of your status update.
:param str source: (optional) The name of application you update the status
    from.
:param int in_reply_to_status_id: (optional) The ID of an existing status that
    the update is in reply to.
:param int lat: (optional) The latitude of the location this status refers to.
    This parameter will be ignored unless it is inside the range -90.0 to
    +90.0 (North is positive) inclusive. It will also be ignored if there
    isn’t a corresponding long parameter.
:param int long: (optional) The longitude of the location this tweet refers to.
    The valid ranges for longitude is -180.0 to +180.0 (East is positive)
    inclusive. This parameter will be ignored if outside that range, if
    it is not a number or if there not a corresponding lat parameter.
:param str media: (optional) the name of the file to upload with the status.
:rtype: dict
:return: dict with following structure:

::

    {status_dict}
    """
    media = None
    if 'media' in kwargs:
        media = {'media': open(kwargs['media'], 'rb').read()}
    kwargs['status'] = status
    return _post_request(server_url=server_url,
                         resource_path='statuses/update',
                         username=username,
                         password=password,
                         data=kwargs,
                         media=media).json()


@docstring(server_url=_SERVER_URL_DOC,
           username=_USERNAME_DOC,
           password=_PASSWORD_DOC,
           status_id=_STATUS_ID_DOC,
           status_dict=_STATUS_DICT)
def show(server_url: str,
         status_id: int,
         username: str='',
         password: str='') -> dict:
    """Returns a single status, specified by the id parameter. The status'
author will also be embedded within the status.

:param str server_url: {server_url}
:param int status_id: {status_id}
:param str username: (optional) {username}
:param str password: (optional) {password}
:rtype: dict
:return: dict with following structure:

::

    {status_dict}
    """
    return _get_request(server_url=server_url,
                        resource_path='statuses/show/%d' % status_id,
                        username=username,
                        password=password).json()


@docstring(server_url=_SERVER_URL_DOC,
           username=_USERNAME_DOC,
           password=_PASSWORD_DOC,
           status_id=_STATUS_ID_DOC,
           status_dict=_STATUS_DICT)
def destroy(server_url: str,
            username: str,
            password: str,
            status_id: int) -> dict:
    """Destroys the status specified by the required ID parameter.
The authenticating user must be the author of the specified status.
Returns the destroyed status if successful.

:param str server_url: {server_url}
:param str username: {username}
:param str password: {password}
:param int status_id: {status_id}
:rtype: dict
:return: dict with following structure:

::

    {status_dict}
    """
    return _post_request(server_url=server_url,
                         resource_path='statuses/destroy/%d' % status_id,
                         username=username,
                         password=password).json()


@docstring(server_url=_SERVER_URL_DOC,
           username=_USERNAME_DOC,
           password=_PASSWORD_DOC,
           status_id=_STATUS_ID_DOC,
           status_dict=_STATUS_DICT)
def repeat(server_url: str,
           username: str,
           password: str,
           status_id: int) -> dict:
    """Repeats a status. Returns the original status with repeat details
embedded.

:param str server_url: {server_url}
:param str username: {username}
:param str password: {password}
:param int status_id: {status_id}
:rtype: dict
:return: dict with following structure:

::

    {status_dict}
    """
    return _post_request(server_url=server_url,
                         resource_path='statuses/retweet/%d' % status_id,
                         username=username,
                         password=password).json()


@docstring(server_url=_SERVER_URL_DOC,
           username=_USERNAME_DOC,
           password=_PASSWORD_DOC,
           since_id=_SINCE_ID_DOC,
           max_id=_MAX_ID_DOC,
           count=_STATUSES_COUNT,
           status_dict=_STATUS_DICT)
def conversation(server_url: str,
                 conversation_id: int,
                 username: str='',
                 password: str='',
                 **kwargs) -> list:
    """Returns statuses that have been posted in the conversation.

:param str server_url: {server_url}
:param int conversation_id: The ID of the conversation.
:param str username: (optional) {username}
:param str password: (optional) {password}
:param int since_id: (optional) {since_id}
:param int max_id: (optional) {max_id}
:param int count: (optional) {count}
:rtype: list
:return: list of dicts with following structure:

::

    {status_dict}
    """
    resource_path = 'statusnet/conversation/%d' % conversation_id
    return _get_request(server_url=server_url,
                        resource_path=resource_path,
                        username=username,
                        password=password,
                        params=kwargs).json()
