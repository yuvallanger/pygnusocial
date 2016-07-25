from .utils import _post_request, _get_request
from .utils import _check_user_target, _check_group_id_and_name


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
                         data=kwargs).json()


def show(server_url: str,
         username: str='',
         password: str='',
         **kwargs) -> dict:
    resource_path = _resource_path('statusnet/groups/show', **kwargs)
    return _get_request(server_url=server_url,
                        resource_path=resource_path,
                        username=username,
                        password=password).json()


def create(server_url: str,
           username: str,
           password: str,
           group_name: str) -> dict:
    return _post_request(server_url=server_url,
                         resource_path='statusnet/groups/create',
                         username=username,
                         password=password,
                         data={'nickname': group_name}).json()


def join(server_url: str,
         username: str,
         password: str,
         **kwargs) -> dict:
    resource_path = _resource_path('statusnet/groups/join', **kwargs)
    return _post_request(server_url=server_url,
                         resource_path=resource_path,
                         username=username,
                         password=password,
                         data=kwargs).json()


def leave(server_url: str,
          username: str,
          password: str,
          **kwargs) -> dict:
    resource_path = _resource_path('statusnet/groups/leave', **kwargs)
    return _post_request(server_url=server_url,
                         resource_path=resource_path,
                         username=username,
                         password=password,
                         data=kwargs).json()


def list_all(server_url: str,
             username: str='',
             password: str='') -> list:
    return _get_request(server_url=server_url,
                        resource_path='statusnet/groups/list_all',
                        username=username,
                        password=password).json()


def user_groups(server_url: str,
                username: str='',
                password: str='',
                **kwargs) -> list:
    _check_user_target(**kwargs)
    return _post_request(server_url=server_url,
                         resource_path='statusnet/groups/list',
                         username=username,
                         password=password,
                         data=kwargs).json()


def members(server_url: str,
            username: str='',
            password: str='',
            **kwargs) -> list:
    resource_path = _resource_path('statusnet/groups/membership', **kwargs)
    return _post_request(server_url=server_url,
                         resource_path=resource_path,
                         username=username,
                         password=password,
                         data=kwargs).json()


def is_member(server_url: str,
              username: str='',
              password: str='',
              **kwargs) -> bool:
    _check_user_target(**kwargs)
    _check_group_id_and_name(**kwargs)
    return _post_request(server_url=server_url,
                         resource_path='statusnet/groups/is_member',
                         username=username,
                         password=password,
                         data=kwargs).json()['is_member']
