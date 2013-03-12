.. _development:
.. module:: donottrack.tests
   :synopsis: How to check current build status, run tests locally.

Development
===========

Source Code
-----------

``donottrack`` source code is managed using Git, and can be found on GitHub_.
Feel free to clone, fork, and contribute.

.. _GitHub: https://github.com/benspaulding/django-donottrack/

Documentation
-------------

The documentation is written in plain text, viewable practially anywhere. An
HTML version of the docs can be found online at `Read the Docs`_. If you want
to build a local version of these, you can install Sphinx_, and then from the
``doc`` directory in this repository, run::

    make html

You will find the built docs in the ``docs/_build/html`` directory.

.. _Read The Docs: http://django-donottrack.readthedocs.org/docs/
.. _Sphinx: http://sphinx.pocoo.org/

Tests
-----

|Build status|_

.. |Build status| image::
   https://secure.travis-ci.org/benspaulding/django-donottrack.png
.. _Build status: http://travis-ci.org/benspaulding/django-donottrack

``donottrack`` has a full test suite. Current build status can be found at
`Travis CI`_.

.. _Travis CI: http://travis-ci.org/benspaulding/django-donottrack

Test settings are included, so tests can be run outside of a Django project::

    django-admin.py test donottrack --settings="donottrack.tests.settings"

If you have not installed ``donottrack``, but are working from a Git checkout,
you will need to either have it on your ``PYTHONPATH`` or run the above command
from the root of the repository.

.. note:: In order for ``donottrack`` tests to run in your project, you will
          need to add ``donottrack`` to your ``INSTALLED_APPS``. (Mentioned
          here because no other ``donottrack`` functionality requires this.)

