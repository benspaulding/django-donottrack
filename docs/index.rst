.. _index:
.. module:: donottrack

Django Do Not Track
===================

Overview
--------

|Build status|_

.. |Build status| image::
   https://secure.travis-ci.org/benspaulding/django-donottrack.png
.. _Build status: https://travis-ci.org/benspaulding/django-donottrack

Django utilities for honoring the `Do Not Track HTTP header`_.

`Mathieu Leplatre`_ posted an article |Do not forget DNT|_. I really
appreciated the post, and wanted to implement the ideas in my projects. Being
lazy, I only wanted to do the work once, so I took his ideas and packaged them
up with some tests and docs.

Included is middleware for detecting ``HTTP_DNT`` and passing its information
on to both views and templates via the ``request`` object, and a useful
context processor. The middleware also adds a vary header for cache control.

This package requires Python 2.7 or newer and Django 1.4 or later.

.. _Do Not Track HTTP header: http://donottrack.us/
.. _Mathieu Leplatre: https://twitter.com/leplatrem
.. |Do not forget DNT| replace:: `Django: Do not forget Do Not Track`
.. _Do not forget DNT:
    http://blog.mathieu-leplatre.info/django-do-not-forget-do-not-track.html


Contents
--------

.. toctree::
   :maxdepth: 2

   getting-started
   development


Indices and tables
------------------

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`

