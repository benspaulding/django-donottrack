# -*- coding: utf-8 -*-

"""
Settings for running app tests when not part of another project.

"""

from __future__ import unicode_literals


# Requred by Django, though we don't actually use the database.
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': ':memory:',
    }
}

INSTALLED_APPS = (
    'donottrack',
)

# Again, required by Django.
SECRET_KEY = 'super-secret!'
