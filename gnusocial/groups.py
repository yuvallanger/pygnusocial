from .utils import _check_id_and_nickname, _post_request, _get_request


def _resource_path(resource_path: str, **kwargs):
    if 'id' in kwargs:
        resource_path += '/%d' % kwargs['id']
    elif 'nickname' in kwargs:
        resource_path += '/%s' % kwargs['nickname']
    else:
        raise Exception(
            "You must either specify the id or nickname."
        )
    return resource_path


def timeline(server_url: str,
             username: str='',
             password: str='',
             **kwargs) -> list:
    _check_id_and_nickname(**kwargs)
    resource_path = _resource_path('statusnet/groups/timeline', **kwargs)
    return _post_request(server_url=server_url,
                         resource_path=resource_path,
                         username=username,
                         password=password,
                         data=kwargs)


def show(server_url: str,
         username: str='',
         password: str='',
         **kwargs) -> dict:
    _check_id_and_nickname(**kwargs)
    resource_path = _resource_path('statusnet/groups/show', **kwargs)
    return _get_request(server_url=server_url,
                        resource_path=resource_path,
                        username=username,
                        password=password)
