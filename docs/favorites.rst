.. include:: strings.rst
Favorites
=========

.. module:: favorites

.. function:: create(server_url, status_id, *, username='', password='', oauth={})

  Favorites the status specified in the ID parameter as the authenticating
  user. Returns the liked status when successful.

  :param str server_url: |server_url|
  :param int status_id: ID of the status to delete
  :param str username: |username|
  :param str password: |password|
  :param dict oauth: |oauth|
  :rtype: dict
  :return: :ref:`status_dict`


.. function:: destroy(server_url, status_id, *, username='', password='', oauth={})

   Unfavorites the status specified in the ID parameter as the authenticating
   user. Returns the unliked status when successful.

  :param str server_url: |server_url|
  :param int status_id: ID of the status to delete
  :param str username: |username|
  :param str password: |password|
  :param dict oauth: |oauth|
  :rtype: dict
  :return: :ref:`status_dict`

.. function:: favorites(server_url, *, since_id=None, max_id=None, count=20, username='', password='', oauth={})

  Returns recent notices favorited by the authenticating or specified user.

  :param str server_url: |server_url|
  :param int since_id: |status_since_id|
  :param int max_id: |status_max_id|
  :param int count: |status_count|
  :param str username: |username|
  :param str password: |password|
  :param dict oauth: |oauth|
  :rtype: list
  :return: a list of :ref:`status dicts <status_dict>`
