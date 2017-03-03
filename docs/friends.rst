.. include:: strings.rst
Friends
=======

.. module:: friends


.. function:: friends(server_url, *, user_id=None, screen_name=None, count=20, username='', password='', oauth={})

  Returns IDs of users the auntenticated or specified user is following
  (otherwise known as their "friends").

  :param str server_url: |server_url|
  :param int user_id: |user_id|
  :param str screen_name: |screen_name|
  :param int count: |user_count|
  :param str username: |username|
  :param str password: |password|
  :param dict oauth: |oauth|
  :rtype: list
  :return: a list of user IDs


.. function:: followers(server_url, *, user_id=None, screen_name=None, count=20, username='', password='', oauth={})

  Returns IDs of users the auntenticated or specified user is followed by.

  :param str server_url: |server_url|
  :param int user_id: |user_id|
  :param str screen_name: |screen_name|
  :param int count: |user_count|
  :param str username: |username|
  :param str password: |password|
  :param dict oauth: |oauth|
  :rtype: list
  :return: a list of user IDs
