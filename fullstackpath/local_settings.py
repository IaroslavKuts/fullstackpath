import os
import posixpath


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

SECRET_KEY = ''

DEBUG = True

ALLOWED_HOSTS = []

DATABASES = {   
    'default':{
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'DjangoTest',
        'USER' : 'postgres',
        'PASSWORD' : 'sisma',
        'HOST' : '127.0.0.1',
        'PORT' : '5432'
        }
}

STATIC_URL = '/static/'
STATIC_ROOT = posixpath.join(*(BASE_DIR.split(os.path.sep) + ['static']))