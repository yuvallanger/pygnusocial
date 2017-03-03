from .decorators import post

@post
def create(**kwargs):
    return {'resource_path': 'blocks/create', 'data': kwargs}


@post
def destroy(**kwargs):
    return {'resource_path': 'blocks/destroy', 'data': kwargs}
