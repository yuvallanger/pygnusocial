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


def read(file):
    with open(file) as f:
        return f.read()

setup(name='ostatus',
      version='1.0',
      description='',
      long_description=read('README'),
      author='dtluna',
      author_email='dtluna@openmailbox.org',
      maintainer='dtluna',
      maintainer_email='dtluna@openmailbox.org',
      license='GPLv3',
      keywords=[''],
      classifiers=[
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: Implementation',
      ],
      url='https://gitgud.io/dtluna/',
      platforms=['any'],
      packages=['ostatus'],
      requires=['requests'],
      )
