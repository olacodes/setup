import dj_database_url
from decouple import config
from .base import *

SECRET_KEY = config('SECRET_KEY')

DEBUG = False
DATABASES = {
  'default': {
    **dj_database_url(config('DATABASE_URL')),
    'ENGINE': 'django.db.backends.postgresql',
  }
}
