"""
gnusocial.docs
~~~~~~~~~~~~~~

Module with common docstring constants.
"""

_SERVER_URL_DOC = 'URL of the server'
_USERNAME_DOC = 'name of the authenticating user'
_PASSWORD_DOC = 'password of the authenticating user'
_NAME_DOC = 'full name associated with the profile'
_URL_DOC = '''URL associated with the profile.
        Will be prepended with "http://" if not present'''
_FULLNAME_DOC = 'full name associated with the group'
_HOMEPAGE_DOC = 'home page URL associated with the group'
_ALIASES_DOC = 'aliases that group has'

_LOCATION_DOC = '''The city or country describing
        where the %s is located.
        The contents are not normalized or geocoded in any way'''
_USER_LOCATION = _LOCATION_DOC % 'user of the account'
_GROUP_LOCATION = _LOCATION_DOC % 'group'

_DESCRIPTION_DOC = 'A description of the %s'
_USER_DESCRIPTION = _DESCRIPTION_DOC % 'user owning the account'
_GROUP_DESCRIPTION = _DESCRIPTION_DOC % 'group'

_PROFILE_LINK_COLOR_DOC = '''Sets a hex value that controls the
        color scheme of links used on the authenticating user’s profile page.
        This must be a valid hexadecimal value,
        and may be either three or six characters (ex: F00 or FF0000).'''
_SCREEN_NAME_DOC = '''The screen name of the user for whom to
        return results for.'''
_USER_ID_DOC = '''The ID of the user for whom to return results
        for. '''

_COUNT_DOC = '''Specifies the number of %s to try
        and retrieve. If not provided, defaults
        to 20.'''
_USERS_COUNT = _COUNT_DOC % 'users'
_DM_COUNT = _COUNT_DOC % 'direct messages'
_STATUSES_COUNT = _COUNT_DOC % 'statuses'
_GROUP_COUNT = _COUNT_DOC % 'groups'

_MAX_ID_DOC = '''Returns results with an ID less than
        (that is, older than) or equal to the specified ID.'''
_SINCE_ID_DOC = '''Returns results with an ID greater than
        (that is, more recent than) the specified ID.'''
_TEXT_DOC = 'The text of your direct message.'
_STATUS_ID_DOC = 'The numerical ID of the desired status.'
_TARGET_USER_DOC = 'User that is followed. Can be an ID or screen name.'
_SOURCE_USER_DOC = 'User that is following. Can be an ID or screen name.'
_SOURCE_ID_DOC = 'The user_id of the subject user.'
_SOURCE_SCREEN_NAME_DOC = 'The screen_name of the subject user.'
_TARGET_ID_DOC = 'The user_id of the target user.'
_TARGET_SCREEN_NAME_DOC = 'The screen_name of the target user.'
_GROUP_ID_DOC = '''The ID of the group for which to return
        results for.'''
_GROUP_NAME_DOC = '''The name of the group for which to return
        results for.'''
_CONFIG_DICT = """{
        'attachments':
        {
            'file_quota': int, # maximum size of attachment in bytes
            'uploads': bool # True if users are allowed to upload files
        },
        'group':
        {
            'desclimit': int
        },
        'integration':
        {
            'source': str
        },
        'license':
        {
            'image': str,
            'owner': str,
            'title': str,
            'type': str,
            'url': str
        },
        'nickname':
        {
            'featured': list
        },
        'notice':
        {
            'contentlimit': int
        },
        'profile':
        {
            'biolimit': int
        },
        'site':
        {
            'broughtby': str,
            'broughtbyurl': str,
            'closed': bool,
            'email': str,
            'fancy': str,
            'inviteonly': bool,
            'language': str,
            'logo': str,
            'name': str,
            'path': str,
            'private': bool,
            'server': str,
            'ssl': str,
            'sslserver': str,
            'textlimit': str,
            'theme': str,
            'timezone': str
        },
        'throttle':
        {
            'count': int,
            'enabled': bool,
            'timespan': int
        },
        'url':
        {
            'maxnoticelength': int,
            'maxurllength': int
        },
        'xmpp':
        {
            'enabled': bool,
            'port': int,
            'server': str,
            'user': str
        }
    }"""

_USER_DICT = """{
        'background_image': str, # URL to background image or False if none
        'backgroundcolor': str, # background color in hex or False if default
        'cover_photo': str, # URL to cover image or False if none
        'created_at': str, # the date of user registration
        'description': str, # user profile description or False if none
        'favourites_count': int, # the number of notices favorited by user
        'followers_count': int,
        'following': bool, # True if authenticating user is following the user
        'friends_count':int, # the number of users user is following
        'groups_count': int, # the number of group user is member of
        'id': int,
        'is_local': bool, # True if user is from server_url
        'is_sandboxed': bool,
        'is_silenced': bool,
        'linkcolor': str, # link color in hex or False if default
        'location': str, # user's location or False if none
        'name': str, # full name associated with the profile
        'notifications': bool, # True if authenticating user is getting
                               # notifications from user
        'ostatus_uri': str, # URL to user profile
        'profile_background_color':str, # same as backgroundcolor
        'profile_banner_url': str, # same as cover_photo
        'profile_image_url': str, # URL to 48x48 avatar image
        'profile_image_url_https': str. # same as profile_image_url, but with
                                        # HTTPS
        'profile_image_url_original': str, # URL to avatar image in original
                                           # resolution
        'profile_image_url_profile_size': str, # URL to 96x96 avatar image
        'profile_link_color': str, # same as linkcolor
        'protected': bool,
        'rights': # a dict of what user can do
        {
            'delete_others_notice': bool,
            'delete_user': bool,
            'sandbox': bool,
            'silence': bool
        },
        'screen_name': str, # user's handle
        'status': dict, # user's latest status
        'statuses_count': int,
        'statusnet_blocking': bool,
        'statusnet_profile_url': str,
        'time_zone': str,
        'url': str, # URL associated with the profile or False if none
        'utc_offset': str
    }"""

_DM_DICT = '''{
        'created_at': str, # date of message creation
        'id': int,
        'recipient': dict, # user dict
        'recipient_id': int,
        'recipient_screen_name': str,
        'sender': dict, # user dict
        'sender_id': int,
        'sender_screen_name': str,
        'text': str
    }'''

_STATUS_DICT = '''{
        'attachments':
        [
            {
                'height': str,
                'id': str,
                'large_thumb_url': str,
                'mimetype': str,
                'oembed': bool,
                'size': str, # size of attacment in kilobytes
                'thumb_url': str,
                'url': str,
                'version': str,
                'width': str
            }
        ],
        'attentions':
        [
            {
                'fullname': str,
                'id': int,
                'ostatus_uri': str,
                'profileurl': str,
                'screen_name': str
            }
        ],
        'created_at': str,
        'external_url': str,
        'fave_num': int, # number of users favorited the notice
        'favorited': bool, # True if favorited by authenticated user
        'geo': str,
        'id': int,
        'in_reply_to_ostatus_uri': str,
        'in_reply_to_profileurl': str,
        'in_reply_to_screen_name': str,
        'in_reply_to_status_id': str,
        'in_reply_to_user_id': int,
        'is_local': bool,
        'is_post_verb': bool,
        'repeat_num': int,
        'repeated': bool, # True if repeated by authenticated user
        'repeated_id': int,
        'retweeted_status': dict, # repeated status dict
        'source': str,
        'statusnet_conversation_id': int,
        'statusnet_html': str, # HTML contents of the notice
        'statusnet_in_groups': bool,
        'text': str, # plain text contents of the notice
        'truncated': bool,
        'uri': str,
        'user': dict # user dict
    }'''

_RELATIONSHIP_DICT = '''{
        'relationship':
        {
            'source':
            {
                'blocking': bool, # True if source user is blocking target user
                'followed_by': bool, # True if source user is followed by
                                     # target user
                'following': bool, # True if source user is following target
                                   # user
                'id': int,
                'notifications_enabled': bool, # If notifications about target
                                               # user are enabled for source
                                               # user
                'screen_name': str
            },
            'target': dict # same as source
        }
    }'''

_GROUP_DICT = '''{
        'admin_count': int,
        'blocked': bool,
        'created': str,
        'description': str,
        'fullname': str,
        'homepage': str,
        'homepage_logo': str,
        'id': int.
        'location': str,
        'member': bool,
        'member_count': int,
        'mini_logo': str,
        'modified': str,
        'nickname': str,
        'original_logo': str,
        'stream_logo': str,
        'url': str
    }'''
