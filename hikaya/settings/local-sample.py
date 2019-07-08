from base import *

from fabric.api import cd, env, run

NOTIFICATION_SENDER = os.getenv('NOTIFICATION_SENDER')

# See: https://docs.djangoproject.com/en/dev/ref/settings/#managers
MANAGERS = ADMINS
########## END MANAGER CONFIGURATION

########## DEBUG CONFIGURATION
# See: https://docs.djangoproject.com/en/dev/ref/settings/#debug
DEBUG = True #if os.getenv('HIKAYA_DEBUG') == 'True' else False

########## END DEBUG CONFIGURATION


############ MONGO DB #####################
MONGODB_DATABASES = {
    "default": {
        "name": os.getenv("HIKAYATABLES_MONGODB_NAME"),
        "host": os.getenv("HIKAYATABLES_MONGODB_HOST", '127.0.0.1'),
        "port": int(os.getenv("HIKAYATABLES_MONGODB_PORT", 27017)),
        "username": os.getenv("HIKAYATABLES_MONGODB_USER"),
        "password": os.getenv("HIKAYATABLES_MONGODB_PASS"),
    },
}
MONGO_URI = 'mongodb://{username}:{password}@{host}:{port}/{db}'.format(
    db=MONGODB_DATABASES['default']['name'],
    username=MONGODB_DATABASES['default']['username'],
    password=MONGODB_DATABASES['default']['password'],
    host=MONGODB_DATABASES['default']['host'],
    port=MONGODB_DATABASES['default']['port'],
)
################ END OF MONGO DB #######################


########## DATABASE CONFIGURATION
# See: https://docs.djangoproject.com/en/dev/ref/settings/#databases
try:
    DATABASES = {
        'default': {
            'ENGINE': os.getenv('HIKAYATABLES_DB_ENGINE', 'django.db.backends.postgresql'),
            'NAME': os.getenv('HIKAYATABLES_DB_NAME', ''),
            'USER': os.getenv('HIKAYATABLES_DB_USER', ''),
            'PASSWORD': os.getenv('HIKAYATABLES_DB_PASS', ''),
            'HOST': os.getenv('HIKAYATABLES_DB_HOST', ''),
            'PORT': os.getenv('HIKAYATABLES_DB_PORT', 5432),
        }
    }
except KeyError:
    # Fallback for tests without environment variables configured
    # Depends on os.environ for correct functionality
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': 'hikaya_tables',
        }
    }
    print("DATABASES: {}".format(DATABASES))
########## END DATABASE CONFIGURATION

# Hosts/domain names that are valid for this site
if os.getenv('HIKAYA_HOSTNAME') is not None:
    ALLOWED_HOSTS = os.environ['HIKAYA_HOSTNAME'].split(',')

USE_X_FORWARDED_HOST = True if os.getenv('HIKAYA_USE_X_FORWARDED_HOST') == 'True' else False

########## GOOGLE CLIENT CONFIG ###########
if os.getenv('TABLES_URL') is not None:
    GOOGLE_REDIRECT_URL = os.getenv('TABLES_URL') + '/oauth2callback/'
else:
    GOOGLE_REDIRECT_URL = 'http://localhost:8000/oauth2callback/'

if os.getenv('GOOGLE_ANALYTICS') is not None:
    GOOGLE_ANALYTICS = os.getenv('GOOGLE_ANALYTICS')
else:
    GOOGLE_ANALYTICS = None


####### Tola Activity API #######
HIKAYA_ACTIVITY_API_URL = os.getenv('HIKAYA_ACTIVITY_API_URL', '')
HIKAYA_ACTIVITY_API_TOKEN = os.getenv('HIKAYA_ACTIVITY_API_TOKEN')

########## CACHE CONFIGURATION
# See: https://docs.djangoproject.com/en/dev/ref/settings/#caches
CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
    }
}
########## END CACHE CONFIGURATION


########## END CACHE CONFIGURATION

try:
    template_dir = os.environ['HIKAYATABLES_TEMPLATE_DIR']
except KeyError:
    template_dir = "templates2"

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [normpath(join(SITE_ROOT, 'templates2')), ],
        # 'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.template.context_processors.debug',
                'django.template.context_processors.i18n',
                'django.template.context_processors.media',
                'django.template.context_processors.static',
                'django.template.context_processors.tz',
                'django.contrib.messages.context_processors.messages',
                'hikaya.context_processors.get_silos',
                'hikaya.context_processors.get_servers',
                'hikaya.context_processors.google_oauth_settings',
                'hikaya.context_processors.google_analytics',
            ],
            'builtins': [
                'django.contrib.staticfiles.templatetags.staticfiles',
                'silo.templatetags.underscoretags',
            ],
            'loaders': [
                'django.template.loaders.filesystem.Loader',
                'django.template.loaders.app_directories.Loader',
            ]
        },
    },
]

APP_BRANCH = os.getenv('APP_BRANCH')
ACTIVITY_URL = os.getenv('ACTIVITY_URL')
TABLES_URL = os.getenv('TABLES_URL')
TABLES_LOGIN_URL = '/accounts/login'

SOCIAL_AUTH_HIKAYA_KEY = os.getenv('SOCIAL_AUTH_HIKAYA_KEY')
SOCIAL_AUTH_HIKAYA_SECRET = os.getenv('SOCIAL_AUTH_HIKAYA_SECRET')

CELERY_BROKER_URL = os.getenv('CELERY_BROKER_URL')
CELERY_RESULT_BACKEND = os.getenv('CELERY_BROKER_URL')

# Hosts to deploy onto
env.hosts = ['.hikayadata.io', '.hikaya.io']

# Where your project code lives on the server
env.project_root = DJANGO_ROOT


def deploy_static():
    with cd(env.project_root):
        run('./manage.py collectstatic -v0 --noinput')


GOOGLE_API_KEY = os.getenv('GOOGLE_API_KEY')
GOOGLE_OAUTH_CLIENT_ID = os.getenv('GOOGLE_OAUTH_CLIENT_ID')
GOOGLE_OAUTH_CLIENT_SECRET = os.getenv('GOOGLE_OAUTH_CLIENT_SECRET')

ONEDRIVE_CLIENT_ID = os.getenv('ONEDRIVE_CLIENT_ID')
ONEDRIVE_REDIRECT_URI = os.getenv('ONEDRIVE_REDIRECT_URI')

# This allows for additional settings to be kept in a local file
try:
    from local_secret import *
except ImportError:
    pass
