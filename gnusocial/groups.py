from .utils import _post_request, _get_request


def _resource_path(resource_path: str, **kwargs):
    group_id = kwargs.get('id')
    group_name = kwargs.get('nickname')
    if bool(group_id) == bool(group_name):
        raise Exception(
            "You must either specify the id or nickname."
        )
    if group_id:
        resource_path += '/%d' % group_id
    if group_name:
        resource_path += '/%s' % group_name
    return resource_path


def timeline(server_url: str,
             username: str='',
             password: str='',
             **kwargs) -> list:
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
    resource_path = _resource_path('statusnet/groups/show', **kwargs)
    return _get_request(server_url=server_url,
                        resource_path=resource_path,
                        username=username,
                        password=password)
