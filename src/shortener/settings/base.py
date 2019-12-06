import os

from shortener.utils import config_loader
from . import ENVIRONMENT

# region constants

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PROJECT_DIR = os.path.dirname(os.path.dirname(BASE_DIR))
CONFIG_DIR = os.path.join(PROJECT_DIR, 'config')

# endregion

# region config

CONFIG = config_loader.load_config_directory(CONFIG_DIR, ENVIRONMENT)

# endregion

# region Secret Key

SECRET_KEY = CONFIG['iam']['secretKey']

# endregion

# region django setup

INSTALLED_APPS = [
    # Django Apps
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'rest_framework',

    'shortener.apps.iam.apps.IamConfig',
    'shortener.apps.client.apps.ClientConfig',
    'shortener.apps.link.apps.LinkConfig',
    'shortener.apps.analytics.apps.AnalyticsConfig',
]

MIDDLEWARE = [
    # Django Security Middleware
    'django.middleware.security.SecurityMiddleware',

    # Django Middleware
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',

    'shortener.apps.iam.middlewares.AuthenticationMiddleware',
]

ROOT_URLCONF = 'shortener.urls'

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

WSGI_APPLICATION = 'shortener.wsgi.application'

REST_FRAMEWORK = {
    'EXCEPTION_HANDLER': 'shortener.errors.error_handler',
}

# endregion

# region authentication

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

# endregion

# region internationalization

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# endregion

# region static and media files

MEDIA_ROOT = os.path.join(PROJECT_DIR, 'media/')

STATICFILES_DIRS = (os.path.join(PROJECT_DIR, 'static/'),)

STATIC_ROOT = os.path.join(PROJECT_DIR, 'static_files/')
STATIC_URL = '/static/'

MEDIA_URL = '/media/'

# endregion

REDIS = {
    'HOST': 'localhost',
    'PORT': 6379,
    'PASSWORD': '',
    'DB': 1,
}

RABBITMQ = {
    'URL': 'pyamqp://localhost:5672'
}