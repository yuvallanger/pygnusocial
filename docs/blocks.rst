.. include:: strings.rst
Blocking
========

.. module:: blocks

.. function:: create(server_url, *, user_id=None, screen_name=None, username='', password='', oauth={})

  Blocks the specified user from following the authenticating user.
  In addition the blocked user will not show in the authenticating users
  mentions or timeline (unless repeated by another user). If a follow or
  friend relationship exists it is destroyed.

  :param str server_url: |server_url|
  :param int user_id: (optional) the ID of the user to block
  :param str screen_name: (optional) the handle of the user to block
  :param str username: |username|
  :param str password: |password|
  :param dict oauth: |oauth|
  :rtype: dict
  :return: :ref:`user_dict`


.. function:: destroy(server_url, *, user_id=None, screen_name=None, username='', password='', oauth={})

  Un-blocks the specified user from following the authenticating user.
  If relationships existed before the block was instated,
  they will not be restored.

  :param str server_url: |server_url|
  :param int user_id: (optional) the ID of the user to un-block
  :param str screen_name: (optional) the handle of the user to un-block
  :param str username: |username|
  :param str password: |password|
  :param dict oauth: |oauth|
  :rtype: dict
  :return: :ref:`user_dict`
