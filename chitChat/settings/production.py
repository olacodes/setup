import dj_database_url
from decouple import config
from .base import *



BASE_DIR = Path(__file__).resolve().parent.parent.parent

DEBUG = False
DATABASES = {
  'default': {
    **dj_database_url.parse(config('DATABASE_URL')),
    'ENGINE': 'django.db.backends.postgresql',
  }
}

STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'