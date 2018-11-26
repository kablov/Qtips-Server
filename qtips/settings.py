import os
from .database_settings import SecretKeys


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

ACCESS_KEY = "JBVFDWH9pFp7MKQWfzLdxtLxYka0fZ9j"

SECRET_KEY = 'cyjc9&j)5sj*u^%5b484(+k^0w2yff-si-+1r*-#t1g4f98ugg'

DEBUG = True

ALLOWED_HOSTS = [
    '127.0.0.1',
    'qtips-prod.herokuapp.com'
]


INSTALLED_APPS = [
    'api.apps.ApiConfig',

    'rest_framework',

    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'qtips.urls'


TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'qtips.wsgi.application'


DATABASES = SecretKeys.DATABASE_PRODUCTION
CLOUDINARY = SecretKeys.CLOUDINARY_PRODUCTION


AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


LANGUAGE_CODE = 'ru-ru'

TIME_ZONE = 'Europe/Moscow'

USE_I18N = True

USE_L10N = True

USE_TZ = True


STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')


TWILIO_ACCOUNT_SID = "AC9fc8bf64e0f96d06e254e9962a6f0a6f"
TWILIO_AUTH_TOKEN = "46d6c4f7b46652dfe1420cd5179bfcd8"
TWILIO_FROM_NUMBER = "+16148812580"
