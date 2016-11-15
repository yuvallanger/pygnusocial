"""
gnusocial.oauth
~~~~~~~~~~~~~~~

Module with OAuth resources.
"""
from urllib.parse import parse_qs
from dtd import docstring
from requests_oauthlib import OAuth1
from .utils import _post_request, _resource_url
from .docs import _SERVER_URL_DOC

_CONSUMER_KEY = """A value used by the application to identify itself to the GNU
    Social server"""
_CONSUMER_SECRET = """A secret used by the application to establish ownership of
    the consumer key"""
_RESOURCE_OWNER_KEY = """A key used by user to authorize"""
_RESOURCE_OWNER_SECRET = """A secret used by the application to establish
    ownership of a given token"""
_RESOURCE_OWNER_DICT = """dict with 'resource_owner_key' and
    'resource_owner_secret' keys"""


def _parse_response(response) -> dict:
    creds = parse_qs(response.text)
    res = {}
    res['resource_owner_key'] = creds['oauth_token'][0]
    res['resource_owner_secret'] = creds['oauth_token_secret'][0]
    return res


@docstring(server_url=_SERVER_URL_DOC,
           consumer_key=_CONSUMER_KEY,
           consumer_secret=_CONSUMER_SECRET,
           resource_owner_dict=_RESOURCE_OWNER_DICT)
def request_token(server_url: str,
                  consumer_key: str,
                  consumer_secret: str,
                  oauth_callback: str='oob') -> dict:
    """Returns resource owner key and secret for given consumer key and secret.

:param str server_url: {server_url}
:param str consumer_key: {consumer_key}
:param str consumer_secret: {consumer_secret}
:param str oauth_callback: (optional) A callback URL
:rtype: dict
:return: {resource_owner_dict}
    """
    oauth = OAuth1(client_key=consumer_key, client_secret=consumer_secret)
    return _parse_response(_post_request(
        server_url=server_url,
        resource_path='oauth/request_token',
        oauth=oauth,
        data={'oauth_callback': oauth_callback},
        extension=''
    ))


@docstring(server_url=_SERVER_URL_DOC,
           resource_owner_key=_RESOURCE_OWNER_KEY)
def authorize_url(server_url: str,
                  resource_owner_key: str) -> str:
    """Returns a URL used to obtain user authorization for application access.

:param str server_url: {server_url}
:param str resource_owner_key: {resource_owner_key}
:rtype: str
:return: a URL used to obtain user authorization for application access
    """
    return _resource_url(server_url, 'oauth/authorize', extension='') +\
        '?oauth_token=' + resource_owner_key


@docstring(server_url=_SERVER_URL_DOC,
           consumer_key=_CONSUMER_KEY,
           consumer_secret=_CONSUMER_SECRET,
           resource_owner_key=_RESOURCE_OWNER_KEY,
           resource_owner_secret=_RESOURCE_OWNER_SECRET,
           resource_owner_dict=_RESOURCE_OWNER_DICT)
def access_token(server_url: str,
                 consumer_key: str,
                 consumer_secret: str,
                 resource_owner_key: str,
                 resource_owner_secret: str,
                 secret_key: str) -> dict:
    """Returns access key and secret.

:param str server_url: {server_url}
:param str consumer_key: {consumer_key}
:param str consumer_secret: {consumer_secret}
:param str oauth_callback: (optional) A callback URL
:rtype: dict
:return: {resource_owner_dict}
    """
    oauth = OAuth1(client_key=consumer_key,
                   client_secret=consumer_secret,
                   resource_owner_key=resource_owner_key,
                   resource_owner_secret=resource_owner_secret,
                   verifier=secret_key)
    return _parse_response(_post_request(
        server_url=server_url,
        resource_path='oauth/access_token',
        oauth=oauth
    ))
