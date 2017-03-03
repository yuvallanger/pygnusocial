.. include:: strings.rst
Exceptions
==========

.. module:: exceptions

.. exception:: AuthenticationError(server_url, username, password)

  Exception class for authentication errors.

  :param str server_url: |server_url|
  :param str username: |username|


.. exception:: GNUSocialAPIError(error_message)

  Exception class for API errors.

  :param str error_message: API error message

.. exception:: ServerURLError(server_url)

  Exception class for invalid server URLs.

  :param str server_url: |server_url|
