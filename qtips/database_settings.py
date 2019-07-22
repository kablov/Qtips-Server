import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

DATABASE_PRODUCTION_PASSWORD = os.environ['DATABASE_PRODUCTION_PASSWORD']
CLOUDINARY_PRODUCTION_API_KEY = os.environ['CLOUDINARY_PRODUCTION_API_KEY']


class SecretKeys:
    DATABASE_PRODUCTION = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql_psycopg2',
            'NAME': 'd4pphab2mh9g8n',
            'USER': 'kpbtmaogzpoacz',
            'PASSWORD': DATABASE_PRODUCTION_PASSWORD,
            'HOST': 'ec2-54-228-248-66.eu-west-1.compute.amazonaws.com',
            'PORT': '5432',
            'TEST': {
                'NAME': 'd4q1dhf384mutg',
            },
            }
    }

    DATABASE_TEST = {
       'default': {
           'ENGINE': 'django.db.backends.sqlite3',
           'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
        }
    }

    CLOUDINARY_PRODUCTION = {
        'cloud_name': 'dbuvm0sag',
        'api_key': CLOUDINARY_PRODUCTION_API_KEY,
        'api_secret': 'F2zzgQP27QXIHdD8KERZO7WC4rE',
    }
