from .base import *
import dj_database_url
from decouple import config


DEBUG = False
DATABASES = {
  'default': {
    **dj_database_url(config('DATABASE_URL')),
    'ENGINE': 'django.db.backends.postgresql',
  }
}
