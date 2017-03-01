from .decorators import get, post

@get
def received(**kwargs):
    return {'resource_path': 'direct_messages', 'params': kwargs}


@get
def sent(**kwargs):
    return {'resource_path': 'direct_messages/sent', 'params': kwargs}


@post
def new(text, **kwargs):
    kwargs['text'] = text
    return {'resource_path': 'direct_messages/new', 'data': kwargs}
