from xml.etree import ElementTree as ET
from .utils import _post_request


def upload(server_url: str,
           username: str,
           password: str,
           filename: str) -> str:
    media = {'media': open(filename, 'rb')}
    response_xml = _post_request(server_url=server_url,
                                 resource_path='statusnet/media/upload',
                                 extension='',
                                 username=username,
                                 password=password,
                                 media=media).text
    tree = ET.fromstring(response_xml)
    return tree.find('{http://www.w3.org/2005/Atom}link').get('href')
