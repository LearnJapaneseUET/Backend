import os
from .settings import *
from .settings import BASE_DIR

ALLOWED_HOSTS = [os.environ['CUSTOM_DOMAIN']]
CSRF_TRUSTED_ORIGINS = ['https://'+os.environ['CUSTOM_DOMAIN']]
DEBUG = False
SECRET_KEY = os.environ['SECRET_KEY']

MIDDLEWARE = [
    "corsheaders.middleware.CorsMiddleware",
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

CORS_ALLOWED_ORIGINS = ['https://'+os.environ['CUSTOM_DOMAIN']]

CORS_ALLOW_CREDENTIALS = True
CORS_ALLOW_METHODS = [
    'DELETE',
    'GET',
    'OPTIONS',
    'PATCH',
    'POST',
    'PUT',
]


STORAGES = {
    "default": {
        "BACKEND": "django.core.files.storage.FileSystemStorage",
    },
    "staticfiles": {
        "BACKEND": "whitenoise.storage.CompressedStaticFilesStorage",
    },
}


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': config('DB_NAME', default='default_db_name'),
        'USER': config('DB_USER', default='default_db_user'),
        'PASSWORD': config('DB_PASSWORD', default='default_password'),
        'HOST': config('DB_HOST', default='localhost'),
        'PORT': config('DB_PORT', default='5432'),
    }
}

STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
