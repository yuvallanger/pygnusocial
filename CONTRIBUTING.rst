Development installation
------------------------

1. Clone this repository (preferably to a virtualenv):

``git clone https://gitgud.io/dtluna/pygnusocial``

2. Install needed development dependencies:

``pip install -r requirements.txt``

3. Install ``gnusocial`` package in development mode:

``pip install -e .``


Testing
-------
Run ``./runtests.py``

The tests are situated in ``tests`` directory.

Tests are written using `Pytest <http://docs.pytest.org/en/latest/>`_.

Building docs
-------------

``cd docs && make html``

Docs are written using `Sphinx <http://www.sphinx-doc.org/en/stable/>`_.