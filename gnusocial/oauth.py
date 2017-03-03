from functools import partial
from urllib.parse import parse_qs

from .decorators import post
from .utils import _resource_url

def _parse_response(response):
    creds = parse_qs(response.text)
    res = {}
    res['resource_owner_key'] = creds['oauth_token'][0]
    res['resource_owner_secret'] = creds['oauth_token_secret'][0]
    return res


def _make_oauth_dict(consumer_key, consumer_secret, response):
    creds = _parse_response(response)
    creds.update({
        'consumer_key': consumer_key,
        'consumer_secret': consumer_secret
    })
    return creds


@post
def request_token(consumer_key, consumer_secret):
    return {'resource_path': 'oauth/request_token', 'extension': '',
            'oauth': {
                'consumer_key': consumer_key,
                'consumer_secret': consumer_secret,
            },
            'data': {'oauth_callback': 'oob'},
            'postprocessor': partial(_make_oauth_dict, consumer_key,
                                     consumer_secret)}


def authorize_url(server_url, resource_owner_key):
    return _resource_url(server_url, 'oauth/authorize', extension='') +\
        '?oauth_token=' + resource_owner_key


@post
def access_token(consumer_key, consumer_secret, resource_owner_key,
                 resource_owner_secret, secret_key):
    oauth = {'consumer_key': consumer_key,
             'consumer_secret': consumer_secret,
             'resource_owner_key':resource_owner_key,
             'resource_owner_secret': resource_owner_secret,
             'secret_key': secret_key}
    return {'resource_path': 'oauth/access_token', 'extension': '',
            'oauth': oauth,
            'postprocessor': partial(_make_oauth_dict, consumer_key,
                                     consumer_secret)}
