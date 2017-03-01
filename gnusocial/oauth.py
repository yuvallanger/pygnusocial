from functools import partial
from urllib.parse import parse_qs
from requests_oauthlib import OAuth1

from .decorators import post
from .utils import _resource_url

def _parse_response(response):
    creds = parse_qs(response.text)
    res = {}
    res['resource_owner_key'] = creds['oauth_token'][0]
    res['resource_owner_secret'] = creds['oauth_token_secret'][0]
    return res


def _make_oauth_object(consumer_key, consumer_secret, response):
    return OAuth1(client_key=consumer_key, client_secret=consumer_secret,
                  **_parse_response(response))


@post
def request_token(consumer_key, consumer_secret):
    oauth = OAuth1(client_key=consumer_key, client_secret=consumer_secret)
    return {'resource_path': 'oauth/request_token', 'extension': '', 'oauth': oauth,
            'data': {'oauth_callback': 'oob'}, 'postprocessor': _parse_response}


def authorize_url(server_url, resource_owner_key):
    return _resource_url(server_url, 'oauth/authorize', extension='') +\
        '?oauth_token=' + resource_owner_key


@post
def access_token(consumer_key, consumer_secret, resource_owner_key,
                 resource_owner_secret, secret_key):
    oauth = OAuth1(client_key=consumer_key,
                   client_secret=consumer_secret,
                   resource_owner_key=resource_owner_key,
                   resource_owner_secret=resource_owner_secret,
                   verifier=secret_key)
    return {'resource_path': 'oauth/access_token', 'extension': '', 'oauth': oauth,
            'postprocessor': partial(_make_oauth_object, consumer_key, consumer_secret)}
