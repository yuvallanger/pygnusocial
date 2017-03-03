.. include:: strings.rst
Timelines
=========

.. module:: timelines

.. function:: public(server_url, *, since_id=None, max_id=None, count=20, username='', password='', oauth={})

  Returns the most recent notices, including repeats if they exist, from
  non-protected users.

  :param str server_url: |server_url|
  :param int since_id: |status_since_id|
  :param int max_id: |status_max_id|
  :param int count: |status_count|
  :param str username: |username|
  :param str password: |password|
  :param dict oauth: |oauth|
  :rtype: list
  :return: a list of :ref:`status dicts <status_dict>`

.. function:: home(server_url, *, since_id=None, max_id=None, count=20, username='', password='', oauth={})

  Returns the most recent notices, including repeats if they exist,
  posted by the authenticating user and the users they follow.

  :param str server_url: |server_url|
  :param int since_id: |status_since_id|
  :param int max_id: |status_max_id|
  :param int count: |status_count|
  :param str username: |username|
  :param str password: |password|
  :param dict oauth: |oauth|
  :rtype: list
  :return: a list of :ref:`status dicts <status_dict>`

.. function:: friends(server_url, *, user_id=None, screen_name=None, since_id=None, max_id=None, count=20, username='', password='', oauth={})

  Home timeline for the specified user.

  :param str server_url: |server_url|
  :param int user_id: |user_id|
  :param str screen_name: |screen_name|
  :param int since_id: |status_since_id|
  :param int max_id: |status_max_id|
  :param int count: |status_count|
  :param str username: |username|
  :param str password: |password|
  :param dict oauth: |oauth|
  :rtype: list
  :return: a list of :ref:`status dicts <status_dict>`

.. function:: user(server_url, *, user_id=None, screen_name=None, since_id=None, max_id=None, count=20, username='', password='', oauth={})

  Returns the most recent notices posted by the authenticating user. It
  is also possible to request another user's timeline by using the
  ``screen_name`` or ``user_id`` parameter. The other users timeline will only
  be visible if they are not protected, or if the authenticating user's follow
  request was accepted by the protected user.

  :param str server_url: |server_url|
  :param int user_id: |user_id|
  :param str screen_name: |screen_name|
  :param int since_id: |status_since_id|
  :param int max_id: |status_max_id|
  :param int count: |status_count|
  :param str username: |username|
  :param str password: |password|
  :param dict oauth: |oauth|
  :rtype: list
  :return: a list of :ref:`status dicts <status_dict>`

.. function:: mentions(server_url, *, user_id=None, screen_name=None, since_id=None, max_id=None, count=20, username='', password='', oauth={})

  Returns the most recent mentions (notices containing @username) for
  the authenticating user or specified user.

  :param str server_url: |server_url|
  :param int user_id: |user_id|
  :param str screen_name: |screen_name|
  :param int since_id: |status_since_id|
  :param int max_id: |status_max_id|
  :param int count: |status_count|
  :param str username: |username|
  :param str password: |password|
  :param dict oauth: |oauth|
  :rtype: list
  :return: a list of :ref:`status dicts <status_dict>`

.. function:: replies(server_url, *, user_id=None, screen_name=None, since_id=None, max_id=None, count=20, username='', password='', oauth={})

  Returns the most recent mentions (notices containing @username) for
  the authenticating user or specified user.

  :param str server_url: |server_url|
  :param int user_id: |user_id|
  :param str screen_name: |screen_name|
  :param int since_id: |status_since_id|
  :param int max_id: |status_max_id|
  :param int count: |status_count|
  :param str username: |username|
  :param str password: |password|
  :param dict oauth: |oauth|
  :rtype: list
  :return: a list of :ref:`status dicts <status_dict>`
