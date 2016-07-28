"""
gnusocial.statuses
~~~~~~~~~~~~~~~~~~

Module with status resources.
"""
from .utils import _post_request, _get_request, docstring
from .docs import (SERVER_URL_DOC, USERNAME_DOC, PASSWORD_DOC, STATUS_DICT,
                   STATUS_ID_DOC)


@docstring(server_url=SERVER_URL_DOC,
           username=USERNAME_DOC,
           password=PASSWORD_DOC,
           status_dict=STATUS_DICT)
def update(server_url: str,
           username: str,
           password: str,
           status: str,
           **kwargs) -> dict:
    """Updates the authenticating user's current status.

    :param server_url: {server_url}
    :param username: {username}
    :param password: {password}
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
    :param media: (optional) the name of the file to upload with the status.
    :return: dict with following structure:
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


@docstring(server_url=SERVER_URL_DOC,
           username=USERNAME_DOC,
           password=PASSWORD_DOC,
           status_id=STATUS_ID_DOC,
           status_dict=STATUS_DICT)
def show(server_url: str,
         status_id: int,
         username: str='',
         password: str='') -> dict:
    """Returns a single status, specified by the id parameter. The status'
        author will also be embedded within the status.

    :param server_url: {server_url}
    :param status_id: {status_id}
    :param username: (optional) {username}
    :param password: (optional) {password}
    :return: dict with following structure:
        {status_dict}
    """
    return _get_request(server_url=server_url,
                        resource_path='statuses/show/%d' % status_id,
                        username=username,
                        password=password).json()


@docstring(server_url=SERVER_URL_DOC,
           username=USERNAME_DOC,
           password=PASSWORD_DOC,
           status_id=STATUS_ID_DOC,
           status_dict=STATUS_DICT)
def destroy(server_url: str,
            username: str,
            password: str,
            status_id: int) -> dict:
    """Destroys the status specified by the required ID parameter.
        The authenticating user must be the author of the specified status.
        Returns the destroyed status if successful.

    :param server_url: {server_url}
    :param username: {username}
    :param password: {password}
    :param status_id: {status_id}
    :return: dict with following structure:
        {status_dict}
    """
    return _post_request(server_url=server_url,
                         resource_path='statuses/destroy/%d' % status_id,
                         username=username,
                         password=password).json()


@docstring(server_url=SERVER_URL_DOC,
           username=USERNAME_DOC,
           password=PASSWORD_DOC,
           status_id=STATUS_ID_DOC,
           status_dict=STATUS_DICT)
def repeat(server_url: str,
           username: str,
           password: str,
           status_id: int) -> dict:
    """Repeats a status. Returns the original status with repeat details
        embedded.

    :param server_url: {server_url}
    :param username: {username}
    :param password: {password}
    :param status_id: {status_id}
    :return: dict with following structure:
        {status_dict}
    """
    return _post_request(server_url=server_url,
                         resource_path='statuses/retweet/%d' % status_id,
                         username=username,
                         password=password).json()
