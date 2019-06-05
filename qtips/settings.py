import os
from .database_settings import SecretKeys


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

ACCESS_KEY = os.environ['ACCESS_KEY']

SECRET_KEY = 'cyjc9&j)5sj*u^%5b484(+k^0w2yff-si-+1r*-#t1g4f98ugg'

DEBUG = False

ALLOWED_HOSTS = [
    '127.0.0.1',
    'qtips-prod.herokuapp.com',
    'www.qtips.ru',
    'qtips.ru'
]


INSTALLED_APPS = [
    'api.apps.ApiConfig',

    'rest_framework',

    'fcm_django',

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
        'DIRS': [
            os.path.join(BASE_DIR, 'api/templates')
        ],
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


TWILIO_ACCOUNT_SID = os.environ['TWILIO_ACCOUNT_SID']
TWILIO_AUTH_TOKEN = os.environ['TWILIO_AUTH_TOKEN']
TWILIO_FROM_NUMBER = os.environ['TWILIO_FROM_NUMBER']

#TWILIO_ACCOUNT_SID = "ACf02c296c2718cd120c74880820cdbfd8"
#TWILIO_AUTH_TOKEN = "5c9cf2511d23eef057392f34f3512b79"
#TWILIO_FROM_NUMBER = "+14242738489"

FCM_DJANGO_SETTINGS = {
        "FCM_SERVER_KEY": "AAAAoKc7x6c:APA91bHwC4sVm20u5yuWLdxCMpSBwZlqnB01Bd-_uRa7otsIQz-7glPldMOYjQa56HzBhGkdBxKcwy4FgEIwKjnm0a3Oi1afC4dK0my1kxxivVzfW4cOv5_w8KJV_Zi-tltL2pWlg63C",
}

#SCANOVA_API_KEY = os.environ['SCANOVA_API_KEY']
SCANOVA_API_KEY = '0e5797b7251f772f4e2c60eeacecd64136edb36b'
