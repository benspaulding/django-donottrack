# -*- coding: utf-8 -*-

import os

from distutils.core import setup


here = os.path.dirname(__file__)


def get_long_desc():
    return open(os.path.join(here, 'README.rst')).read()


# Function borrowed from carljm.
def get_version():
    fh = open(os.path.join(here, 'donottrack', '__init__.py'))
    try:
        for line in fh.readlines():
            if line.startswith('__version__ ='):
                return line.split('=')[1].strip().strip("'")
    finally:
        fh.close()


setup(
    name='django-donottrack',
    version=get_version(),
    description='Django utilities for honoring the Do Not Track HTTP header.',
    url='https://github.com/benspaulding/django-donottrack/',
    author='Ben Spaulding',
    author_email='ben@benspaulding.us',
    license='BSD',
    download_url='https://github.com/benspaulding/django-donottrack/tarball/v{0}'.format(get_version()),
    long_description=get_long_desc(),
    packages=[
        'donottrack',
        'donottrack.tests',
    ],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Topic :: Internet :: WWW/HTTP :: Browsers',
        'Topic :: Internet :: WWW/HTTP :: Site Management',
    ],
)
