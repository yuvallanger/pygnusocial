Data structures
===============

.. _oauth_dict:

OAuth dict
----------

A dict to pass as the ``oauth`` argument to any function except ones in
:mod:`oauth` module to use for authentication.

Dicts of this structure are returned by :func:`oauth.request_token` and
:func:`oauth.access_token`.

::

  {
      'consumer_key': 'dbd6f083ba50cd1a061ab114f35a5d83',
      'consumer_secret':'16bb8da66e5b4404721a17e44e74b18d',
      'resource_owner_key': '66b3c0ce86e231fb0b014dcba5c51c47',
      'resource_owner_secret': 'e261a7e968c9156972e7b1dc677686c4',
  }

.. _user_dict:

User dict
---------

A dict describing a GNU Social user. Returned by functions in
:mod:`accounts`, :mod:`blocks`, :mod:`users` modules and also
:func:`friendships.create` and :func:`friendships.destroy`.

::

  {
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
  }

.. _status_dict:

Status dict
-----------

::

  {
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
  }

.. _group_dict:

Group dict
----------

::

  {
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
  }

.. _relationship_dict:

Relationship dict
-----------------

::

  {
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
  }

.. _dm_dict:

Direct message dict
-------------------

A dict returned by functions in :mod:`direct_messages` module.

::

  {
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
  }

.. _config_dict:

Config dict
-----------

A dict describing configuration of a GNU Social instance. Returned by
:func:`config.config`.

::

  {
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
  }


.. _as_dict:

ActivityStream dict
--------------------

A dict returned by functions in :mod:`activity_streams` module.

::

  {
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
                'id': str, # Example: 'tag:gs.smuglo.li,2016-11-16:noticeId=1028155:objectType=comment'
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
                'id': str, # Example: 'tag:gs.smuglo.li,2016-11-16:noticeId=1028155:objectType=comment'
                'inReplyTo':
                {
                    'id': str, # Example: 'tag:gs.smuglo.li,2016-11-16:noticeId=1028155:objectType=comment'
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
                'conversation': str, # Example:tag:social.heldscal.la,2016-11-15:objectType=thread:nonce=c53d340f4850ca73 ,
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
