from .base import *

ALLOWED_HOSTS = ['*']

DEBUG = True

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(PROJECT_DIR, 'db.sqlite3'),
    }
}

LOGGING = {
    'version': 1,
    'disable_existing_loggers': True,
    'formatters': {
        'standard': {
            'format': "%(asctime)s %(levelname)s: %(message)s",
            'datefmt': "[%Y/%b/%d %H:%M:%S]"
        },
    },
    'handlers': {
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'standard',
        },
        'logfile': {
            'level': 'DEBUG',
            'class': 'logging.handlers.TimedRotatingFileHandler',
            'filename': PROJECT_DIR + '/logs/project.log',
            'when': 'D',
            'interval': 1,
            'backupCount': 20,
            'formatter': 'standard',
        },
    },
    'loggers': {
        'django': {
            'handlers': ['console', 'logfile', ],
            'propagate': True,
            'level': 'WARN',
        },
        'django.db.backends': {
            'handlers': [],
            'propagate': False,
            'level': 'DEBUG',
        },
        'django.request': {
            'handlers': ['console', ],
            'level': 'DEBUG',
            'propagate': False,
        },
        'shortener': {
            'handlers': ['console', 'logfile', ],
            'level': 'DEBUG',
        },
    }
}
