import os

from django.core.exceptions import ImproperlyConfigured
import dj_database_url

from cityyouthmatrix.settings.base import *   # noqa


DEBUG = False
TEMPLATES[0]['OPTIONS'].update({'debug': DEBUG})

ALLOWED_HOSTS = ['cityyouthmatrix.herokuapp.com']

SECRET_KEY = os.getenv('SECRET_KEY')
if not SECRET_KEY:
    raise ImproperlyConfigured('No SECRET_KEY is set!')

db_url = os.getenv('DATABASE_URL')
if not db_url:
    raise ImproperlyConfigured('DATABASE_URL is not set!')
DATABASES['default'] = dj_database_url.parse(
    db_url, 'django.contrib.gis.db.backends.postgis')
