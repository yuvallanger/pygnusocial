.. include:: strings.rst
Statuses
========

.. module:: statuses

.. function:: update(server_url, status, *, source=None, in_reply_to_status_id=None, lat=None, long=None, media=None, username='', password='', oauth={})

  Updates the authenticating user's current status.

  :param str server_url: |server_url|
  :param str status: the text of your status update.
  :param str source: (optional) the name of application you update the status
      from.
  :param int in_reply_to_status_id: (optional) the ID of an existing status that
      the update is in reply to.
  :param int lat: (optional) the latitude of the location this status refers to.
      This parameter will be ignored unless it is inside the range -90.0 to
      +90.0 (North is positive) inclusive. It will also be ignored if there
      isn’t a corresponding long parameter
  :param int long: (optional) the longitude of the location this status refers
      to. The valid ranges for longitude is -180.0 to +180.0 (East is positive)
      inclusive. This parameter will be ignored if outside that range, if
      it is not a number or if there not a corresponding lat parameter
  :param media: (optional) a file like stream of bytes to upload as attachment
  :param str username: |username|
  :param str password: |password|
  :param dict oauth: |oauth|
  :rtype: dict
  :return: :ref:`status_dict`

.. function:: show(server_url, status_id, *, username='', password='', oauth={})

  Returns a specified status.

  :param str server_url: |server_url|
  :param int status_id: ID of the status to show
  :param str username: |username|
  :param str password: |password|
  :param dict oauth: |oauth|
  :rtype: dict
  :return: :ref:`status_dict`

.. function:: destroy(server_url, status_id, *, username='', password='', oauth={})

  Deletes the status specified by the required ID parameter.
  The authenticating user must be the author of the specified status.
  Returns the destroyed status if successful.

  :param str server_url: |server_url|
  :param int status_id: ID of the status to delete
  :param str username: |username|
  :param str password: |password|
  :param dict oauth: |oauth|
  :rtype: dict
  :return: :ref:`status_dict`

.. function:: repeat(server_url, status_id, *, username='', password='', oauth={})

  Repeats a status. Returns the original status with repeat details
  embedded.

  :param str server_url: |server_url|
  :param int status_id: ID of the status to repeat
  :param str username: |username|
  :param str password: |password|
  :param dict oauth: |oauth|
  :rtype: dict
  :return: :ref:`status_dict`

.. function:: conversation(server_url, conversation_id, *, since_id=None, max_id=None, count=20, username='', password='', oauth={})

  Returns statuses that have been posted in the conversation

  :param str server_url: |server_url|
  :param int conversation_id: ID of the conversation to show
  :param int since_id: |status_since_id|
  :param int max_id: |status_max_id|
  :param int count: |status_count|
  :param str username: |username|
  :param str password: |password|
  :param dict oauth: |oauth|
  :rtype: list
  :return: a list of :ref:`status dicts <status_dict>`
