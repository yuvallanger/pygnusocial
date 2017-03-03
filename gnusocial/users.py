from .decorators import get

@get
def following(**kwargs):
    return {'resource_path': 'statuses/friends', 'params': kwargs}


@get
def followers(**kwargs):
    return {'resource_path': 'statuses/followers', 'params': kwargs}


@get
def show(**kwargs):
    return {'resource_path': 'users/show', 'params': kwargs}
