.. include:: strings.rst
Accounts
========

.. module:: accounts

.. function:: verify_credentials(server_url, *, username='', password='', oauth={})

  Tests if supplied user credentials are valid.

  :param str server_url: |server_url|
  :param str username: |username|
  :param str password: |password|
  :param dict oauth: |oauth|
  :raise AuthenticationError: if the supplied credentials are invalid
  :rtype: dict
  :return: :ref:`user_dict`


.. function:: register(server_url, nickname, password, confirm, *, email=None, fullname=None, homepage=None, location=None, bio=None)

  Register a new user.

  :param str server_url: |server_url|
  :param str nickname: name of the new user
  :param str password: desired password
  :param str confirm: password confirmation
  :param str email: (optional) email associated with the new user
  :param str fullname: |full_user_name|
  :param str homepage: |user_url|
  :param str location: |user_location|
  :param str bio: |user_description|
  :rtype: dict
  :return: :ref:`user_dict`


.. function:: update_profile(server_url, *, name=None, url=None, location=None, description=None, profile_link_color=None, username='', password='', oauth={})

  Updates the authenticating user's profile.

  :param str server_url: |server_url|
  :param str name: |full_user_name|
  :param str url: |user_url|
  :param str location: |user_location|
  :param str description: |user_description|
  :param str profile_link_color: (optional) color of the profile links
  :param str username: |username|
  :param str password: |password|
  :param dict oauth: |oauth|
  :rtype: dict
  :return: :ref:`user_dict`

.. function:: update_profile_image(server_url, image *, username='', password='', oauth={})

  Updates the authenticating user's profile image.

  :param str server_url: |server_url|
  :param str username: |username|
  :param str password: |password|
  :param dict oauth: |oauth|
  :param image: (optional) a file-like object to upload as profile image
  :rtype: dict
  :return: :ref:`user_dict`
