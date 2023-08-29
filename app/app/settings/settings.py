from .base import *

APPS = [
    # internal apps
    'core.apps.CoreConfig',
    'web.apps.CoreConfig',
    ]
FRAMEWORKS = [
    # frameworks
    'rest_framework',
    'channels',
]

INSTALLED_APPS += APPS
INSTALLED_APPS += FRAMEWORKS

ASGI_APPLICATION = 'app.asgi.application'




LOGGING = {
    "version": 1,
    "disable_existing_loggers":False,

    "formatters": {
        "verbose": {
            "format": "{levelname} {asctime} {module} {process:d} {thread:d} {message}",
            "style": "{",
        },
        "simple": {
            "format": "{levelname} : {message}",
            "style": "{"
        }
    },
    
    "handlers":{
        "debug_logs":{
            "level":"DEBUG",
            "class": "logging.FileHandler",
            "filename": BASE_DIR / "logs/DEBUG.log",
            "formatter": "simple"
        },
        "warnings_log":{
            "level": "WARNING",
            "class": "logging.FileHandler",
            "filename": BASE_DIR / "logs/WARNING.log",
            "formatter": "verbose"
        },
    },
    "loggers":{
        "":{
            "level": 'DEBUG',
            "handlers":["warnings_log",'debug_logs'],
        },

    }
}

AUTH_USER_MODEL = 'core.User' 