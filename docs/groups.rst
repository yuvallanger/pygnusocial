.. include:: strings.rst
Groups
======

.. module:: groups

.. function:: timeline(server_url, *, id=None, nickname=None, since_id=None, max_id=None, count=20, username='', password='', oauth={})

  Shows a group’s timeline. Similar to other timeline resources.

  :param str server_url: |server_url|
  :param int id: |group_id|
  :param str nickname: |group_name|
  :param int since_id: |status_since_id|
  :param int max_id: |status_max_id|
  :param int count: |status_count|
  :param str username: |username|
  :param str password: |password|
  :param dict oauth: |oauth|
  :rtype: list
  :return: a list of :ref:`status dicts <status_dict>`

.. function:: join(server_url, *, id=None, nickname=None, username='', password='', oauth={})

  Join a group.

  :param str server_url: |server_url|
  :param int id: |group_id|
  :param str nickname: |group_name|
  :param str username: |username|
  :param str password: |password|
  :param dict oauth: |oauth|
  :rtype: dict
  :return: :ref:`group_dict`

.. function:: leave(server_url, *, id=None, nickname=None, username='', password='', oauth={})

  Leave a group.

  :param str server_url: |server_url|
  :param int id: |group_id|
  :param str nickname: |group_name|
  :param str username: |username|
  :param str password: |password|
  :param dict oauth: |oauth|
  :rtype: dict
  :return: :ref:`group_dict`

.. function:: create(server_url, nickname, *, full_name=None, homepage=None, location=None, description=None, aliases=None, username='', password='', oauth={})

  Create a new group.

  :param str server_url: |server_url|
  :param str nickname: name of the new group
  :param str full_name: (optional) full name associated with the group
  :param str homepage: (optional) home page URL associated with the group
  :param str location: (optional) The city or country describing where the
                       group is located. The contents are not normalized or
                       geocoded in any way
  :param str description: (optional) A description of the group
  :param list[str] aliases: (optional) aliases that group has
  :param str username: |username|
  :param str password: |password|
  :param dict oauth: |oauth|
  :rtype: dict
  :return: :ref:`group_dict`

.. function:: show(server_url, *, id=None, nickname=None, username='', password='', oauth={})

  Returns details about the group.

  :param str server_url: |server_url|
  :param int id: |group_id|
  :param str nickname: |group_name|
  :param str username: |username|
  :param str password: |password|
  :param dict oauth: |oauth|
  :rtype: dict
  :return: :ref:`group_dict`

.. function:: list_all(server_url, *, count=20, username='', password='', oauth={})

  List all local groups.

  :param str server_url: |server_url|
  :param int count: |group_count|
  :param str username: |username|
  :param str password: |password|
  :param dict oauth: |oauth|
  :rtype: list
  :return: a list of :ref:`group dicts <group_dict>`

.. function:: user_groups(server_url, *, user_id=None, screen_name=None, count=20, username='', password='', oauth={})

  Show the groups a given user is a member of.

  :param str server_url: |server_url|
  :param int user_id: |user_id|
  :param str screen_name: |screen_name|
  :param int count: |group_count|
  :param str username: |username|
  :param str password: |password|
  :param dict oauth: |oauth|
  :rtype: list
  :return: a list of :ref:`group dicts <group_dict>`

.. function:: members(server_url, *, id=None, nickname=None, count=20, username='', password='', oauth={})

  List the members of a given group.

  :param str server_url: |server_url|
  :param int id: |group_id|
  :param str nickname: |group_name|
  :param int count: |user_count|
  :param str username: |username|
  :param str password: |password|
  :param dict oauth: |oauth|
  :rtype: list
  :return: a list of :ref:`user dicts <user_dict>`

.. function:: is_member(server_url, *, user_id=None, screen_name=None, group_id=None, group_name=None, username='', password='', oauth={})

  :param str server_url: |server_url|
  :param int user_id: |user_id|
  :param str screen_name: |screen_name|
  :param int group_id: |group_id|
  :param str group_name: |group_name|
  :param str username: |username|
  :param str password: |password|
  :param dict oauth: |oauth|
  :rtype: bool
  :return: ``True`` if the user is a member of the group, ``False`` otherwise


.. function:: admins(server_url, *, id=None, nickname=None, count=20, username='', password='', oauth={})

  List the admins of a given group.

  :param str server_url: |server_url|
  :param int id: |group_id|
  :param str nickname: |group_name|
  :param int count: |user_count|
  :param str username: |username|
  :param str password: |password|
  :param dict oauth: |oauth|
  :rtype: list
  :return: a list of :ref:`user dicts <user_dict>`
