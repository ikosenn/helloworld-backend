import logging

from helloworld.config.settings import *   # NOQA

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': ':memory:'
    }
}


# Test optimizations
DEBUG = False
TEMPLATE_DEBUG = False
logging.disable(logging.CRITICAL)
LOGGING['handlers']['syslog'] = LOGGING['handlers']['console']


class DisableMigrations(object):
    """disable migrations during unit tests
    stolen from https://gist.github.com/NotSqrt/5f3c76cd15e40ef62d09

    using ``None`` only works for django 1.9
    https://docs.djangoproject.com/en/1.9/ref/settings/#migration-modules

    The only option is to use a wiered package name so that django thinks that
    it's unmigrated
    https://groups.google.com/forum/#!msg/django-developers/PWPj3etj3-U/kCl6pMsQYYoJ

    This class makes the work of assigning each package in ``INSTALLED_APPS``
    easier by always returning a non-existent package name and returning
    ``True`` for all queries of ``__contains__``
    """

    def __contains__(self, item):
        return True

    def __getitem__(self, item):
        return "notmigrations"

MIGRATION_MODULES = DisableMigrations()
