"""
gnusocial.media
~~~~~~~~~~~~~~~

Module with media resources.
"""
from typing import Tuple
from xml.etree import ElementTree as ET
from .utils import _post_request, docstring
from .docs import _SERVER_URL_DOC, _USERNAME_DOC, _PASSWORD_DOC


@docstring(server_url=_SERVER_URL_DOC,
           username=_USERNAME_DOC,
           password=_PASSWORD_DOC)
def upload(server_url: str,
           username: str,
           password: str,
           filename: str) -> Tuple[str, str]:
    """Uploads media to server and returns attachment URL and file URL.

:param server_url: {server_url}
:param username: {username}
:param password: {password}
:param filename: name of the file to upload
:return: tuple with attachment URL and file URL respectively.
    """
    media = {'media': open(filename, 'rb')}
    response_xml = _post_request(server_url=server_url,
                                 resource_path='statusnet/media/upload',
                                 extension='',
                                 username=username,
                                 password=password,
                                 media=media).text
    tree = ET.fromstring(response_xml)
    file_url = tree.find('{http://www.w3.org/2005/Atom}link').get('href', '')
    attachment_url = tree.findtext('mediaurl')
    return (attachment_url, file_url)
