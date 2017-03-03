from .decorators import get, post


@get
def favorites(**kwargs):
    return {'resource_path': 'favorites', 'params': kwargs}


@post
def create(status_id):
    return {'resource_path': 'favorites/create/%d' % status_id}


@post
def destroy(status_id):
    return {'resource_path': 'favorites/destroy/%d' % status_id}
