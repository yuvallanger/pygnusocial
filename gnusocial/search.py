from .decorators import get

@get
def search(query, **kwargs):
    return {'resource_path': 'search.json?q=%s' % query,
            'extension': ''}
