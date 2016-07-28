"""
gnusocial.docs
~~~~~~~~~~~~~~

Module with common docstring constants.
"""

SERVER_URL_DOC = 'URL of the server'
USERNAME_DOC = 'name of the authenticating user'
PASSWORD_DOC = 'password of the authenticating user'
PROFILE_IMAGE_FILENAME_DOC = 'filename of the new profile picture'
NAME_DOC = 'full name associated with the profile'
URL_DOC = '''URL associated with the profile.
        Will be prepended with "http://" if not present'''
LOCATION_DOC = '''The city or country describing
        where the user of the account is located.
        The contents are not normalized or geocoded in any way'''
DESCRIPTION_DOC = 'A description of the user owning the account'
PROFILE_LINK_COLOR_DOC = '''Sets a hex value that controls the
        color scheme of links used on the authenticating user’s profile page.
        This must be a valid hexadecimal value,
        and may be either three or six characters (ex: F00 or FF0000).'''
SCREEN_NAME_DOC = '''The screen name of the user for whom to
        return results for.'''
USER_ID_DOC = '''The ID of the user for whom to return results
        for. '''
COUNT_DOC = '''Specifies the number of %s to try
        and retrieve.'''
USERS_COUNT = COUNT_DOC % 'users'
DM_COUNT = COUNT_DOC % 'direct messages'
MAX_ID_DOC = '''Returns results with an ID less than
        (that is, older than) or equal to the specified ID.'''
SINCE_ID_DOC = '''Returns results with an ID greater than
        (that is, more recent than) the specified ID.'''
TEXT_DOC = 'The text of your direct message.'
STATUSES_COUNT = COUNT_DOC % 'statuses'
STATUS_ID_DOC = 'The numerical ID of the desired status.'
TARGET_USER_DOC = 'User that is followed. Can be an ID or screen name.'
SOURCE_USER_DOC = 'User that is following. Can be an ID or screen name.'
SOURCE_ID_DOC = 'The user_id of the subject user.'
SOURCE_SCREEN_NAME_DOC = 'The screen_name of the subject user.'
TARGET_ID_DOC = 'The user_id of the target user.'
TARGET_SCREEN_NAME_DOC = 'The screen_name of the target user.'
UPLOAD_FILENAME_DOC = 'name of the file to upload'

CONFIG_DICT = """attachments
        file_quota - maximum size of attachment in bytes
        uploads - True if users are allowed to upload files
    group
        desclimit
    integration
        source
    license
        image
        owner
        title
        type
        url
    nickname
        featured
    notice
        contentlimit
    profile
        biolimit
    site
        broughtby
        broughtbyurl
        closed
        email
        fancy
        inviteonly
        language
        logo
        name
        path
        private
        server
        ssl
        sslserver
        textlimit
        theme
        timezone
    throttle
        count
        enabled
        timespan
    url
        maxnoticelength
        maxurllength
    xmpp
        enabled
        port
        server
        user"""

USER_DICT = """background_image - URL to background image or False if none
        backgroundcolor - background color in hex or False if default
        cover_photo - URL to cover image or False if none
        created_at - the date of user registration
        description - user profile description or False if none
        favourites_count - the number of notices favorited by user
        followers_count
        following - True if authenticating user is following the user
        friends_count - the number of users user is following
        groups_count - the number of group user is member of
        id
        is_local - True if user is from server_url
        is_sandboxed
        is_silenced
        linkcolor - link color in hex or False if default
        location - user's location or False if none
        name - full name associated with the profile
        notifications - True if authenticating user
            is getting notifications from user
        ostatus_uri - URL to user profile
        profile_background_color - same as backgroundcolor
        profile_banner_url - same as cover_photo
        profile_image_url - URL to 48x48 avatar image
        profile_image_url_https - same as profile_image_url, but with HTTPS
        profile_image_url_original - URL to avatar image in original resolution
        profile_image_url_profile_size - URL to 96x96 avatar image
        profile_link_color - same as linkcolor
        protected
        rights - a dict of what user can do:
            delete_others_notice
            delete_user
            sandbox
            silence
        screen_name - user's handle
        status - user's latest status
        statuses_count
        statusnet_blocking
        statusnet_profile_url
        time_zone
        url - URL associated with the profile or False if none
        utc_offset"""

DM_DICT = '''created_at - date of message creation
        id
        recipient - user dict
        recipient_id
        recipient_screen_name
        sender - user dict
        sender_id
        sender_screen_name
        text'''

STATUS_DICT = '''attachment - list of dicts with following structure:
            height
            id
            large_thumb_url
            mimetype
            oembed
            size - size of attacment in kilobytes
            thumb_url
            url
            version
            width
        attentions - list dicts with following structure:
            fullname
            id
            ostatus_uri
            profileurl
            screen_name
        created_at
        external_url
        fave_num - number of users favorited the notice
        favorited -  True if favorited by authenticated user
        geo
        id
        in_reply_to_ostatus_uri
        in_reply_to_profileurl
        in_reply_to_screen_name
        in_reply_to_status_id
        in_reply_to_user_id
        is_local
        is_post_verb
        repeat_num
        repeated - True if repeated by authenticated user
        repeated_id
        retweeted_status - repeated status dict
        source
        statusnet_conversation_id
        statusnet_html - HTML contents of the notice
        statusnet_in_groups
        text - plain text contents of the notice
        truncated
        uri
        user - user dict'''

RELATIONSHIP_DICT = '''relationship - dict with following structure:
            source - dict with following structure:
                blocking - True if source user is blocking target user
                followed_by - True if source user is followed by target user
                following - True if source user is following target user
                id
                notifications_enabled - If notifications about target user
                    are enabled for source user
                screen_name
            target - same as source'''
