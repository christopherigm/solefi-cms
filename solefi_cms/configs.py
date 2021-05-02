import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

environment = None
db_name = 'iguzman'
db_user = 'iguzman'
db_password = 'iguzman'
email_id = 'email@mail.com'
email_password = 'password'

if 'env' in os.environ:
    environment = os.environ['env']
if 'db_name' in os.environ:
    db_name = os.environ['db_name']
if 'db_user' in os.environ:
    db_user = os.environ['db_user']
if 'db_password' in os.environ:
    db_password = os.environ['db_password']
if 'email_id' in os.environ:
    email_id = os.environ['email_id']
if 'email_password' in os.environ:
    email_password = os.environ['email_password']

class Common:
    SITE_HEADER = 'Solefi'
    INDEX_TITLE = 'CMS'
    SITE_TITLE = 'CMS'
    EMAIL_HOST = 'smtp.gmail.com'
    EMAIL_USE_TLS = True
    EMAIL_PORT = 587
    DEBUG = True
    ALLOWED_HOSTS = ['*']
    JWT_ACCESS_EXPIRATION_MINUTES = 300
    JWT_REFRESH_EXPIRATION_MINUTES = 600
    DATABASES = {
        'default': {
        'ENGINE': 'django.contrib.gis.db.backends.postgis',
        'NAME': db_name,
        'USER': db_user,
        'PASSWORD': db_password,
        'HOST': '127.0.0.1',
        'PORT': '5432'
        }
    }
    EMAIL_HOST_USER = email_id
    EMAIL_HOST_PASSWORD = email_password

class LOCAL(Common):
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': os.path.join(BASE_DIR, 'db.sqlite3')
        }
    }

class QA(Common):
    FOO = 'bar'

class STAGING(Common):
    FOO = 'bar'

class MASTER(Common):
    DEBUG = False
    JWT_ACCESS_EXPIRATION_MINUTES = 15
    JWT_REFRESH_EXPIRATION_MINUTES = 30

if environment == 'qa':
    env = QA
elif environment == 'staging':
    env = STAGING
elif environment == 'master':
    env = MASTER
else:
    env = LOCAL
