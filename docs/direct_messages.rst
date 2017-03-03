.. include:: strings.rst
Direct messages
===============

.. module:: direct_messages

.. function:: new(server_url, text, *, user_id=None, screen_name=None, username='', password='', oauth={})

  Sends a new direct message to the specified user from the authenticating user.

  :param str server_url: |server_url|
  :param str text: text of your message
  :param int user_id: (optional) the ID of the recipient
  :param str screen_name: (optional) the handle of the recipient
  :param str username: |username|
  :param str password: |password|
  :param dict oauth: |oauth|
  :rtype: dict
  :return: :ref:`dm_dict`

.. function:: sent(server_url, *, since_id=None, max_id=None, count=20, username='', password='', oauth={})

  Returns the 20 most recent direct messages sent by the authenticating user.
  You can request up to 200 direct messages per call, and only the most recent
  200 DMs will be available using this endpoint.

  :param str server_url: |server_url|
  :param int since_id: |dm_since_id|
  :param int max_id: |dm_max_id|
  :param int count: |dm_count|
  :param str username: |username|
  :param str password: |password|
  :param dict oauth: |oauth|
  :rtype: list
  :return: a list of :ref:`direct message dicts <dm_dict>`

.. function:: received(server_url, *, since_id=None, max_id=None, count=20, username='', password='', oauth={})

  Returns the 20 most recent direct messages sent to the authenticating user.
  You can request up to 200 direct messages per call, and only the most recent
  200 DMs will be available using this endpoint.

  :param str server_url: |server_url|
  :param int since_id: |dm_since_id|
  :param int max_id: |dm_max_id|
  :param int count: |dm_count|
  :param str username: |username|
  :param str password: |password|
  :param dict oauth: |oauth|
  :rtype: list
  :return: a list of :ref:`direct message dicts <dm_dict>`
