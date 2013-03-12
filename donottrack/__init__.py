# -*- coding: utf-8 -*-

"""
Django utilities for honoring the `Do Not Track HTTP header`_.

`Mathieu Leplatre`_ posted an article |Do not forget DNT|_. I really
appreciated the post, and wanted to implement the ideas in my projects. Being
lazy, I only wanted to do the work once, so I took his ideas and packaged them
up with some tests and docs.

Included is middleware for detecting ``HTTP_DNT`` and passing its information
on to both views and templates via the ``request`` object. The middleware also
adds a vary header for cache control.

This package requires Python 2.7 or newer and Django 1.4 or later.

Refer to the documentation_ for further information.

.. _Do Not Track HTTP header: http://donottrack.us/
.. _Mathieu Leplatre : https://twitter.com/leplatrem
.. |Do not forget DNT| replace:: `Django: Do not forget Do Not Track`
.. _Do not forget DNT:
    http://blog.mathieu-leplatre.info/django-do-not-forget-do-not-track.html
.. _documentation: http://django-donottrack.readthedocs.org/

"""

from __future__ import unicode_literals


__version__ = '0.1'
