#!/usr/bin/env python3
# pylint: disable=missing-docstring
import codecs
from setuptools import setup
try:
    codecs.lookup('mbcs')
except LookupError:
    def func(name, enc=codecs.lookup('ascii')):
        return {True: enc}.get(name == 'mbcs')
    codecs.register(func)


setup(name='gnusocial',
      version='2.3.0',
      description='GNU Social API for Python 3',
      long_description=open('README.rst').read(),
      author='dtluna',
      author_email='dtluna@openmailbox.org',
      maintainer='dtluna',
      maintainer_email='dtluna@openmailbox.org',
      license='GPLv3',
      classifiers=[
          'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
          'Operating System :: OS Independent',
          'Programming Language :: Python :: 3',
      ],
      url='https://gitgud.io/dtluna/pygnusocial',
      platforms=['any'],
      packages=['gnusocial'],
      python_requires='>=3.5',
      install_requires=['requests', 'dtd', 'requests-oauthlib'])
