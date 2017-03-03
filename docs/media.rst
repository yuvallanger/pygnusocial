.. include:: strings.rst
Media uploads
=============

.. module:: media

.. function:: upload(server_url, media, *, username='', password='', oauth={})

  Uploads media to server and returns attachment URL and file URL.

  :param str server_url: |server_url|
  :param media: a file like stream of bytes to upload
  :param str username: |username|
  :param str password: |password|
  :param dict oauth: |oauth|
  :rtype: tuple
  :return: tuple with attachment URL and file URL respectively
