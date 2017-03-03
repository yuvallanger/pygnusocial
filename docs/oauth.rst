.. include:: strings.rst
OAuth
=====

.. module:: oauth

.. function:: request_token(server_url, consumer_key, consumer_secret)

   Returns resource owner key and secret for given consumer key and secret.

  :param str server_url: |server_url|
  :param str consumer_key: |consumer_key|
  :param str consumer_secret: |consumer_secret|
  :rtype: dict
  :return: :ref:`oauth_dict`

.. function:: authorize_url(server_url, resource_owner_key)

   Returns a URL used to obtain user authorization for application access.

  :param str server_url: |server_url|
  :param str resource_owner_key: |resource_owner_key|
  :rtype: str
  :return: a URL used to obtain user authorization for application access

.. function:: access_token(server_url, consumer_key, consumer_secret, resource_owner_key, resource_owner_secret, secret_key)

   Returns resource owner key and secret for given consumer key and secret.

  :param str server_url: |server_url|
  :param str consumer_key: |consumer_key|
  :param str consumer_secret: |consumer_secret|
  :param str resource_owner_key: |resource_owner_key|
  :param str resource_owner_secret: |resource_owner_secret|
  :param str secret_key: |secret_key|
  :rtype: dict
  :return: :ref:`oauth_dict`
