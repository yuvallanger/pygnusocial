from functools import wraps

from .utils import _post_request, _get_request

def post(func):
    @wraps(func)
    def _wrapper(server_url, *args, username='', password='',
                 oauth={}, **kwargs):
        request_args = func(*args, **kwargs)
        if 'oauth' in request_args:
            oauth = request_args.pop('oauth')
        postprocessor = request_args.get('postprocessor')
        response = _post_request(
            server_url=server_url,
            username=username,
            password=password,
            oauth=oauth,
            **request_args
        )
        if postprocessor:
            return postprocessor(response)
        else:
            return response
    return _wrapper


def get(func):
    @wraps(func)
    def _wrapper(server_url, *args, username='', password='',
                 oauth={}, **kwargs):
        request_args = func(*args, **kwargs)
        postprocessor = request_args.get('postprocessor')
        response = _get_request(
            server_url=server_url,
            username=username,
            password=password,
            oauth=oauth,
            **request_args
        )
        if postprocessor:
            return postprocessor(response)
        else:
            return response
    return _wrapper
