from .decorators import get, post


def _check_id_and_nickname(**kwargs):
    has_group_id = 'id' in kwargs
    has_group_name = 'nickname' in kwargs
    if has_group_id == has_group_name:
        raise ValueError(
            "You must either specify the id or nickname."
        )


def _resource_path(resource_path, **kwargs):
    _check_id_and_nickname(**kwargs)
    group_id = kwargs.get('id')
    group_name = kwargs.get('nickname')
    if group_id:
        resource_path += '/%d' % group_id
    elif group_name:
        resource_path += '/%s' % group_name
    return resource_path


@get
def timeline(**kwargs):
    resource_path = _resource_path('statusnet/groups/timeline', **kwargs)
    return {'resource_path': resource_path, 'params': kwargs}


@get
def show(**kwargs):
    resource_path = _resource_path('statusnet/groups/show', **kwargs)
    return {'resource_path': resource_path, 'params': kwargs}


@post
def create(nickname, **kwargs):
    kwargs['nickname'] = nickname
    return {'resource_path': 'statusnet/groups/create', 'data': kwargs}


@post
def join(**kwargs):
    resource_path = _resource_path('statusnet/groups/join', **kwargs)
    return {'resource_path': resource_path, 'data': kwargs}


@post
def leave(**kwargs):
    resource_path = _resource_path('statusnet/groups/leave', **kwargs)
    return {'resource_path': resource_path, 'data': kwargs}


@get
def list_all(**kwargs):
    return {'resource_path': 'statusnet/groups/list_all', 'params': kwargs}


@get
def user_groups(**kwargs):
    return {'resource_path': 'statusnet/groups/list', 'params': kwargs}


@get
def members(**kwargs):
    resource_path = _resource_path('statusnet/groups/membership', **kwargs)
    return {'resource_path': resource_path, 'data': kwargs}


@get
def is_member(**kwargs):
    return {'resource_path': 'statusnet/groups/is_member', 'params': kwargs}


@get
def admins(**kwargs):
    resource_path = _resource_path('statusnet/groups/membership', **kwargs)
    return {'resource_path': resource_path, 'data': kwargs}
