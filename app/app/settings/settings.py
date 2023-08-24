from .base import *

APPS = [
    # internal apps
    'core.apps.CoreConfig',
    ]
FRAMEWORKS = [
    # frameworks
    'rest_framework',
    'channels',
]

INSTALLED_APPS += APPS
INSTALLED_APPS += FRAMEWORKS

ASGI_APPLICATION = 'app.asgi.application'
