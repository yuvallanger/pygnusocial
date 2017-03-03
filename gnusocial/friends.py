from .decorators import get

@get
def friends(**kwargs):
    return {'resource_path': 'friends/ids', 'params': kwargs}


@get
def followers(**kwargs):
    return {'resource_path': 'followers/ids', 'params': kwargs}
