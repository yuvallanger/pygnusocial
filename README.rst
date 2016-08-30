pygnusocial
===========

Installation
------------

``pip install gnusocial``

or

``python3 setup.py install``

You can also install ``python-gnusocial`` package from AUR.

Documentation
-------------

Documentation is hosted at https://pythonhosted.org/gnusocial/


Basic usage
-----------


::

>>> from gnusocial import statuses
>>> r = statuses.update('https://gnusocial.server.com', 'username', 'password', "I've just installed #pygnusocial!", source='python3')


If you want to help with the development of pygnusocial, check out the `contribution guide <https://gitgud.io/dtluna/pygnusocial/blob/master/CONTRIBUTING.rst>`_.
