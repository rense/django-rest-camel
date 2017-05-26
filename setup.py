#!/usr/bin/env python
# -*- coding: utf-8 -*-
from codecs import open

from setuptools import setup, find_packages


with open('README.rst') as r:
    readme = r.read()

with open('HISTORY.rst') as h:
    history = h.read().replace('.. :changelog:', '')

long_description = '{}\n\n{}'.format(readme, history)

setup(
    name='django-rest-camel',
    version='0.3.3',
    description='Camel case support for Django REST Framework.',
    long_description=long_description,
    author='Dominik Kozaczko',
    author_email='dominik@kozaczko.info',
    url='https://github.com/dekoza/djangorestframework-camel-case',
    packages=find_packages(),
    license="BSD",
    keywords='djangorestframework_camel django rest camelcase camel',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Natural Language :: English',
        "Programming Language :: Python :: 2",
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
    test_suite='tests',
)
