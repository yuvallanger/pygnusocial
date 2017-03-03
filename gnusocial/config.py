from .decorators import get

@get
def config():
    return {'resource_path': 'statusnet/config'}
