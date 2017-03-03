.. include:: strings.rst
Friendships
===========

.. module:: friendships

.. function:: create(server_url, *, user_id=None, screen_name=None, username='', password='', oauth={})

  Subscribe to status updates from specified user.

  :param str server_url: |server_url|
  :param str username: |username|
  :param str password: |password|
  :param dict oauth: |oauth|
  :param int user_id: (optional) the ID of the user to follow
  :param str screen_name: (optional) the handle of the user to follow
  :rtype: dict
  :return: :ref:`user_dict`


.. function:: destroy(server_url, *, user_id=None, screen_name=None, username='', password='', oauth={})

  Unsubscribe to status updates from specified user.

  :param str server_url: |server_url|
  :param str username: |username|
  :param str password: |password|
  :param dict oauth: |oauth|
  :param int user_id: (optional) the ID of the user to unsubscribe
  :param str screen_name: (optional) the handle of the user to unsubscribe
  :rtype: dict
  :return: :ref:`user_dict`

.. function:: exists(server_url, source_user, target_user, *, username='', password='', oauth={})

  Shows if ``source_user`` follows ``target_user``.

  :param str server_url: |server_url|
  :param source_user: User that is following. Can be an ID or handle
  :type source_user: int or str
  :param target_user: User that is followed. Can be an ID or handle
  :type target_user: int or str
  :param str username: |username|
  :param str password: |password|
  :param dict oauth: |oauth|
  :rtype: bool
  :return: ``True`` if ``source_user`` follows ``target_user``. ``False``
           otherwise.

.. function:: show(server_url, *, source_id=None, source_screen_name=None, target_id=None, target_screen_name=None, username='', password='', oauth={})

  Returns detailed information about the relationship between two
  users.

  :param str server_url: |server_url|
  :param int source_id: (optional) ID of the subject user
  :param str source_screen_name: (optional) handle of the subject user
  :param int target_id: (optional) ID of the target user
  :param str target_screen_name: (optional) handle of the target user
  :param str username: |username|
  :param str password: |password|
  :param dict oauth: |oauth|
  :rtype: dict
  :return: :ref:`relationship_dict`
