from .decorators import get, post

@post
def create(**kwargs):
    return {'resource_path': 'friendships/create', 'data': kwargs}


@post
def destroy(**kwargs):
    return {'resource_path': 'friendships/destroy', 'data': kwargs}


@get
def exists(source_user, target_user):
    return {'resource_path': 'friendships/exists',
            'params': {'user_a': source_user, 'user_b': target_user}}


@get
def show(**kwargs):
    return {'resource_path': 'friendships/show', 'params': kwargs}
