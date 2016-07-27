"""
gnusocial.media
~~~~~~~~~~~~~~~

Module with media resources.
"""
from typing import Tuple
from xml.etree import ElementTree as ET
from .utils import _post_request, docstring
from .docs import (SERVER_URL_DOC, USERNAME_DOC, PASSWORD_DOC,
                   UPLOAD_FILENAME_DOC)


@docstring(server_url=SERVER_URL_DOC,
           username=USERNAME_DOC,
           password=PASSWORD_DOC,
           filename=UPLOAD_FILENAME_DOC)
def upload(server_url: str,
           username: str,
           password: str,
           filename: str) -> Tuple[str, str]:
    """Uploads media to server and returns attachment URL and file URL.

    :param server_url: {server_url}
    :param username: {username}
    :param password: {password}
    :param filename: {filename}
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
