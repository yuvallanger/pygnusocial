from .decorators import post, get

@get
def verify_credentials():
    return {'resource_path': 'account/verify_credentials'}


@post
def update_profile_image(image):
    return {'resource_path': 'account/update_profile_image',
            'files': {'image': image.read()}}


@post
def update_profile(**kwargs):
    return {'resource_path': 'account/update_profile', 'data': kwargs}


@post
def register(nickname, password, confirm, **kwargs):
    kwargs.update({
        'nickname': nickname,
        'password': password,
        'confirm': confirm
    })
    return {'resource_path': 'account/register', 'data': kwargs}
