from .decorators import post, get

@post
def update(status, **kwargs):
    request_dict = dict()

    if kwargs.get('media')
        request_dict['files'] = {'media': kwargs.pop('media').read()}

    if kwargs.get('media_ids')
        media_ids = kwargs.pop('media_ids')
        request_dict['media_ids'] = media_ids

    kwargs['status'] = status

    request_dict['data'] = kwargs

    request_dict['resource_path'] = 'statuses/update'

    return request_dict


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
