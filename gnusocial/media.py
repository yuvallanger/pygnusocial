from xml.etree import ElementTree as ET
from .decorators import post
from .utils import GNUSocialAPIError


@post
def upload(media):
    return {'resource_path': 'statusnet/media/upload', 'extension':'',
            'files': {'media': media.read()},
            'postprocessor': _extract_urls}

def _extract_urls(response):
    response_xml = response.text
    tree = ET.fromstring(response_xml)
    file_url_element = tree.find('{http://www.w3.org/2005/Atom}link')
    if file_url_element is None:
        raise GNUSocialAPIError(tree.find('err').get('msg'))
    else:
        file_url = file_url_element.get('href', '')
        attachment_url = tree.findtext('mediaurl')
        return (attachment_url, file_url)
