.. include:: strings.rst
Search
======

.. module:: search

.. function:: search(server_url, query, *, page=0, rpp=20, callback=None, username='', password='', oauth={})

  Returns a collection of statuses matching a specified query.

  :param str server_url: |server_url|
  :param str query: UTF-8 encoded query
  :param int page: (optional) the page number (starting at 1) to return
  :param int since_id: |status_since_id|
  :param int rpp: (optional) the number of notices to return per page, up to a
      max of 100
  :param str callback: if supplied when using the JSON format, the response will
      use the JSONP format with a callback of the given name
  :param str username: |username|
  :param str password: |password|
  :param dict oauth: |oauth|
  :rtype: list
  :return: a list of :ref:`status dicts <status_dict>`
