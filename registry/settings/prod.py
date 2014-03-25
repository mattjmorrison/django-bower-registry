from registry.settings.base_settings import *

TEMPLATE_DEBUG = DEBUG = False

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': '.local_db',
    }
}

ALLOWED_HOSTS = ['*']
