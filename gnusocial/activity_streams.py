from .decorators import get

@get
def public(**kwargs):
    return {'resource_path': 'statuses/public_timeline',
            'extension': '.as', 'params': kwargs}


@get
def home(**kwargs):
    return {'resource_path': 'statuses/home_timeline',
            'extension': '.as', 'params': kwargs}


@get
def friends(**kwargs):
    return {'resource_path': 'statuses/friends_timeline',
            'extension': '.as', 'params': kwargs}


@get
def user(**kwargs):
    return {'resource_path': 'statuses/user_timeline',
            'extension': '.as', 'params': kwargs}


@get
def mentions(**kwargs):
    return {'resource_path': 'statuses/mentions',
            'extension': '.as', 'params': kwargs}


@get
def replies(**kwargs):
    return {'resource_path': 'statuses/replies',
            'extension': '.as', 'params': kwargs}
