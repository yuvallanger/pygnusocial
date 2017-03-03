.. include:: strings.rst
Users
=====

.. module:: users

.. function:: following(server_url, *, user_id=None, screen_name=None, count=20, username='', password='', oauth={})

  Returns a collection of user objects for users followed by
  the specified user.

  :param str server_url: |server_url|
  :param int user_id: |user_id|
  :param str screen_name: |screen_name|
  :param int count: |user_count|
  :param str username: |username|
  :param str password: |password|
  :param dict oauth: |oauth|
  :rtype: list
  :return: a list of :ref:`user dicts <user_dict>`


.. function:: followers(server_url, *, user_id=None, screen_name=None, count=20, username='', password='', oauth={})

  Unsubscribe to status updates from specified user.

  :param str server_url: |server_url|
  :param int user_id: |user_id|
  :param str screen_name: |screen_name|
  :param int count: |user_count|
  :param str username: |username|
  :param str password: |password|
  :param dict oauth: |oauth|
  :rtype: list
  :return: a list of :ref:`user dicts <user_dict>`


.. function:: show(server_url, *, user_id=None, screen_name=None, username='', password='', oauth={})

  Returns detailed information about the specified user.

  :param str server_url: |server_url|
  :param int user_id: |user_id|
  :param str screen_name: |screen_name|
  :param str username: |username|
  :param str password: |password|
  :param dict oauth: |oauth|
  :rtype: dict
  :return: :ref:`user_dict`
