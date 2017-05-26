=====================================
Django REST Framework CamelCase magic
=====================================

.. image:: https://badge.fury.io/py/django-rest-camel.png
    :target: http://badge.fury.io/py/django-rest-camel
    
.. image:: https://img.shields.io/pypi/v/django-rest-camel.svg
    :target: https://img.shields.io/pypi/v/django-rest-camel.svg


Camel case support for Django REST framework - right now only JSON is supported.

This project is a "resurrection fork" of djangorestframework-camel-case_ by Vitaly Babiy

.. _djangorestframework-camel-case https://github.com/vbabiy/djangorestframework-camel-case

============
Installation
============

At the command line::

    $ pip install django-rest-camel

Add the render and parser to your django settings file.

.. code-block:: python

    # ...
    REST_FRAMEWORK = {

        'DEFAULT_RENDERER_CLASSES': (
            'rest_camel.render.CamelCaseJSONRenderer',
            # Any other renders
        ),

        'DEFAULT_PARSER_CLASSES': (
            'rest_camel.parser.CamelCaseJSONParser',
            # Any other parsers
        ),
    }
    # ...

=============
Running Tests
=============

To run the current test suite, execute the following from the root of he project::

    $ tox

=======
License
=======

* Free software: BSD license
