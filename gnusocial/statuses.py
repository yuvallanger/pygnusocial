from .decorators import post, get

@post
def update(status, **kwargs):
    media = kwargs.get('media')
    if media:
        media = {'media': kwargs.pop('media').read()}
    kwargs['status'] = status
    return {'data': kwargs, 'files': media, 'resource_path': 'statuses/update'}


@get
def show(status_id):
    return {'resource_path': 'statuses/show/%d' % status_id}


@post
def destroy(status_id):
    return {'resource_path': 'statuses/destroy/%d' % status_id}


@post
def repeat(status_id):
    return {'resource_path': 'statuses/retweet/%d' % status_id}

@get
def conversation(conversation_id):
    return {'resource_path': 'statusnet/conversation/%d' % conversation_id}
