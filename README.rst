=====================
 Django Do Not Track
=====================

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

Refer to the documentation_ for complete information.

.. _Do Not Track HTTP header: http://donottrack.us/
.. _Mathieu Leplatre: https://twitter.com/leplatrem
.. |Do not forget DNT| replace:: `Django: Do not forget Do Not Track`
.. _Do not forget DNT:
    http://blog.mathieu-leplatre.info/django-do-not-forget-do-not-track.html
.. _documentation: http://django-donottrack.readthedocs.org/


Quick-Start
-----------

Installation of the middleware is required. The context processor is convenient
and thus recommended.

Settings::

    MIDDLEWARE_CLASSES = (
        # default/other processors ...
        'donottrack.middleware.DoNotTrackMiddleware',
        # default/other processors ...
    )

    TEMPLATE_CONTEXT_PROCESSORS = (
        # default/other processors ...
        'donottrack.context_processors.donottrack',
    )

Then in your template you can do things like::

    {% if not donottrack %}
        {% include "google-analyitcs.html" %}
    {% endif %}

And your views can also handle DNT::

    def my_view(request):
        if not request.donottrack:
            # Log some request data ...

        # continue with view logic

.. tip::

    Adding this app to your ``INSTALLED_APPS`` is currently unnecessary unless
    you want to run tests.


Other Information
-----------------

.. important::

    Installing this app in your Django project does not mean that you honor Do
    Not Track any more than installing django-secure_ means your web
    applicaiton is secure. It only means you have some tools to help with that
    end goal. You will need to audit your full stack to ensure that you are
    honoring DNT. But this app is a great start, and we hope you find it
    useful.

.. _django-secure: https://github.com/carljm/django-secure

.. note::

    This is an initial release. Despite being simple and theoretically solid
    (it has a full test suite) this is a beta-type release, and the public API
    may change, and as I learn more about DNT, more functionality may be added.
