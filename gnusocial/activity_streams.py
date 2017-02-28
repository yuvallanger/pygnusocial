"""
gnusocial.activity_streams
~~~~~~~~~~~~~~~~~~~~~~~~~~

Module with ActivityStream timeline resources
"""
from string import Template
from dtd import docstring
from .utils import _get_request, _check_user_target
from .docs import (_SERVER_URL_DOC, _USERNAME_DOC, _PASSWORD_DOC, _MAX_ID_DOC,
                    _SINCE_ID_DOC, _STATUSES_COUNT, _USER_ID_DOC,
                    _SCREEN_NAME_DOC)


_TAG = '\'tag:gs.smuglo.li,2016-11-16:noticeId=1028155:objectType=comment\''

_TAG_EXAMPLE = 'Example: {tag}'.format(tag=_TAG)

_CONVERSATION_TAG = 'tag:social.heldscal.la,2016-11-15:objectType=thread:' +\
                    'nonce=c53d340f4850ca73'
# TODO: add more verbs
_AS_DICT = Template("""{
        'generator': str, # string describing the server software
        'totalItems': int,
        'title': str, # string describing the result dict
        'links':
        [
            {
                'rel': 'alternate',
                'type': 'text/html',
                'url': str # URL with corresponding content
            }
        ],
        'items':
        [
            {
                'actor':
                {
                    'displayName': str,
                    'id': str, # URL to profile
                    'image':
                    {
                        'height': int,
                        'rel': 'avatar',
                        'type': str, # MIME type
                        'url': str,
                        'width': int
                    },
                    'objectType': 'person',
                    'portablecontacts_net':
                    {
                        'displayName': str,
                        'note': str, # user profile description
                        'preferredUsername': str, # screen name
                        'urls':
                        [
                            {
                                'primary': 'true',
                                'type': 'homepage',
                                'value': str, # URL to the homepage
                            }
                        ]
                    },
                    'status_net':
                    {
                        'avatarLinks':
                        [
                            {
                                'height': int,
                                'rel': 'avatar',
                                'type': str, # MIME type
                                'url': str,
                                'width': int
                            }
                        ],
                        'profile_info':
                        {
                            'local_id': str, # ID of the user on their home server
                        }
                    },
                    'summary': str, # user profile description
                    'url': str,
                },
                'content': str, # status in HTML
                'generator':
                {
                    'id': str, # $tag_example
                    'objectType': 'application',
                    'status_net':
                    {
                        'source_code': 'ostatus'
                    }
                },
                'id': str, #
                'object':
                {
                    'content': str, # status in HTML
                    'id': str, # $tag_example
                    'inReplyTo':
                    {
                        'id': str, # $tag_example
                        'objectType': 'note',
                        'url': str,
                    },
                    'objectType': 'comment',
                    'status_net':
                    {
                        'notice_id': int,
                    },
                    'url': str,
                },
                'provider':
                {
                    'displayName': str,
                    'objectType': 'service',
                    'url': str,
                },
                'published': str, # Example: '2016-11-16T20:42:18+00:00',
                'status_net':
                {
                    'conversation': str, # Example: $conversation_tag,
                    'notice_info':
                    {
                        'local_id': str,
                        'source': 'ostatus'
                    }
                },
                'to': # users, to whom the reply is addressed
                [
                    {
                        'id': str, # URL to profile
                        'objectType': 'http://activitystrea.ms/schema/1.0/person'
                    },
                    {
                        'id': 'http://activityschema.org/collection/public',
                        'objectType': 'http://activitystrea.ms/schema/1.0/collection'
                    }
                ],
                'url': str,
                'verb': str, # Example: 'post'
            }
        ]
    }
""")
_AS_DICT = _AS_DICT.substitute(tag_example=_TAG_EXAMPLE,
                               conversation_tag=_CONVERSATION_TAG)


@docstring(server_url=_SERVER_URL_DOC,
           username=_USERNAME_DOC,
           password=_PASSWORD_DOC,
           since_id=_SINCE_ID_DOC,
           max_id=_MAX_ID_DOC,
           count=_STATUSES_COUNT,
           as_dict=_AS_DICT)
def public(server_url: str,
           username: str='',
           password: str='',
           **kwargs) -> dict:
    """Returns the most recent notices, including repeats if they exist, from
non-protected users.

:param str server_url: {server_url}
:param str username: (optional) {username}
:param str password: (optional) {password}
:param int since_id: (optional) {since_id}
:param int max_id: (optional) {max_id}
:param int count: (optional) {count}
:rtype: dict
:return: dict with following structure:

::

    {as_dict}
    """
    return _get_request(server_url=server_url,
                        resource_path='statuses/public_timeline',
                        extension='.as',
                        username=username,
                        password=password,
                        params=kwargs).json()


@docstring(server_url=_SERVER_URL_DOC,
           username=_USERNAME_DOC,
           password=_PASSWORD_DOC,
           since_id=_SINCE_ID_DOC,
           max_id=_MAX_ID_DOC,
           count=_STATUSES_COUNT,
           as_dict=_AS_DICT)
def home(server_url: str, username: str, password: str, **kwargs) -> list:
    """Returns the most recent notices, including repeats if they exist,
posted by the authenticating user and the users they follow. This is the
same timeline seen by a user when they login to their instance.

:param str server_url: {server_url}
:param str username: (optional) {username}
:param str password: (optional) {password}
:param int since_id: (optional) {since_id}
:param int max_id: (optional) {max_id}
:param int count: (optional) {count}
:rtype: dict
:return: dict with following structure:

::

    {as_dict}
    """
    return _get_request(server_url=server_url,
                        resource_path='statuses/home_timeline',
                        extension='.as',
                        username=username,
                        password=password,
                        params=kwargs).json()


@docstring(server_url=_SERVER_URL_DOC,
           username=_USERNAME_DOC,
           password=_PASSWORD_DOC,
           since_id=_SINCE_ID_DOC,
           max_id=_MAX_ID_DOC,
           count=_STATUSES_COUNT,
           user_id=_USER_ID_DOC,
           screen_name=_SCREEN_NAME_DOC,
           as_dict=_AS_DICT)
def friends(server_url: str,
            username: str='',
            password: str='',
            **kwargs) -> list:
    """Alias of statuses/home_timeline for the specified user.

:param str server_url: {server_url}
:param str username: (optional) {username}
:param str password: (optional) {password}
:param int user_id: (optional) {user_id}
:param str screen_name: (optional) {screen_name}
:param int since_id: (optional) {since_id}
:param int max_id: (optional) {max_id}
:param int count: (optional) {count}
:rtype: dict
:return: dict with following structure:

::

    {as_dict}
    """
    _check_user_target(username, use_username=True, **kwargs)
    return _get_request(server_url=server_url,
                        resource_path='statuses/friends_timeline',
                        extension='.as',
                        username=username,
                        password=password,
                        params=kwargs).json()


@docstring(server_url=_SERVER_URL_DOC,
           username=_USERNAME_DOC,
           password=_PASSWORD_DOC,
           since_id=_SINCE_ID_DOC,
           max_id=_MAX_ID_DOC,
           count=_STATUSES_COUNT,
           user_id=_USER_ID_DOC,
           screen_name=_SCREEN_NAME_DOC,
           as_dict=_AS_DICT)
def user(server_url: str,
         username: str='',
         password: str='',
         **kwargs) -> list:
    """Returns the most recent notices posted by the authenticating user. It
is also possible to request another user's timeline by using the
screen_name or user_id parameter. The other users timeline will only be
visible if they are not protected, or if the authenticating user's follow
request was accepted by the protected user.

:param str server_url: {server_url}
:param str username: (optional) {username}
:param str password: (optional) {password}
:param int user_id: (optional) {user_id}
:param str screen_name: (optional) {screen_name}
:param int since_id: (optional) {since_id}
:param int max_id: (optional) {max_id}
:param int count: (optional) {count}
:rtype: dict
:return: dict with following structure:

::

    {as_dict}
    """
    _check_user_target(username, use_username=True, **kwargs)
    return _get_request(server_url=server_url,
                        resource_path='statuses/user_timeline',
                        extension='.as',
                        username=username,
                        password=password,
                        params=kwargs).json()


@docstring(server_url=_SERVER_URL_DOC,
           username=_USERNAME_DOC,
           password=_PASSWORD_DOC,
           since_id=_SINCE_ID_DOC,
           max_id=_MAX_ID_DOC,
           count=_STATUSES_COUNT,
           user_id=_USER_ID_DOC,
           screen_name=_SCREEN_NAME_DOC,
           as_dict=_AS_DICT)
def mentions(server_url: str,
             username: str='',
             password: str='',
             **kwargs) -> list:
    """Returns the most recent mentions (notices containing @username) for
the authenticating user or specified user.

:param str server_url: {server_url}
:param str username: (optional) {username}
:param str password: (optional) {password}
:param int user_id: (optional) {user_id}
:param str screen_name: (optional) {screen_name}
:param int since_id: (optional) {since_id}
:param int max_id: (optional) {max_id}
:param int count: (optional) {count}
:rtype: dict
:return: dict with following structure:

::

    {as_dict}
    """
    _check_user_target(username, use_username=True, **kwargs)
    return _get_request(server_url=server_url,
                        resource_path='statuses/mentions',
                        extension='.as',
                        username=username,
                        password=password,
                        params=kwargs).json()


@docstring(server_url=_SERVER_URL_DOC,
           username=_USERNAME_DOC,
           password=_PASSWORD_DOC,
           since_id=_SINCE_ID_DOC,
           max_id=_MAX_ID_DOC,
           count=_STATUSES_COUNT,
           user_id=_USER_ID_DOC,
           screen_name=_SCREEN_NAME_DOC,
           as_dict=_AS_DICT)
def replies(server_url: str,
            username: str='',
            password: str='',
            **kwargs) -> list:
    """Alias of statuses/mentions

:param str server_url: {server_url}
:param str username: (optional) {username}
:param str password: (optional) {password}
:param int user_id: (optional) {user_id}
:param str screen_name: (optional) {screen_name}
:param int since_id: (optional) {since_id}
:param int max_id: (optional) {max_id}
:param int count: (optional) {count}
:rtype: dict
:return: dict with following structure:

::

    {as_dict}
    """
    _check_user_target(username, use_username=True, **kwargs)
    return _get_request(server_url=server_url,
                        resource_path='statuses/replies',
                        extension='.as',
                        username=username,
                        password=password,
                        params=kwargs).json()
