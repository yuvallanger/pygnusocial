#!/usr/bin/env python3
import codecs
from setuptools import setup
try:
    codecs.lookup('mbcs')
except LookupError:
    ascii = codecs.lookup('ascii')

    def func(name, enc=ascii):
        return {True: enc}.get(name == 'mbcs')
    codecs.register(func)


setup(name='gnusocial',
      version='1.0',
      description='GNU Social API for Python 3',
      author='dtluna',
      author_email='dtluna@openmailbox.org',
      maintainer='dtluna',
      maintainer_email='dtluna@openmailbox.org',
      license='GPLv3',
      classifiers=[
          'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
          'Natural Language :: English',
          'Operating System :: OS Independent',
          'Programming Language :: Python :: 3',
      ],
      url='https://gitgud.io/dtluna/pygnusocial',
      platforms=['any'],
      packages=['gnusocial'],
      requires=['requests'],
      )
