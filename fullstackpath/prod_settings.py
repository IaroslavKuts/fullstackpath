import os
import posixpath


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

SECRET_KEY = ''

DEBUG = False

ALLOWED_HOSTS = ["127.0.0.1"]

DATABASES = {   
    'default':{
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'DjangoTestUser',
        'USER' : 'postgres',
        'PASSWORD' : 'sisma',
        'HOST' : 'localhost',
        'PORT' : '5432'
        }
}

STATIC_ROOT = posixpath.join(*(BASE_DIR.split(os.path.sep) + ['static']))