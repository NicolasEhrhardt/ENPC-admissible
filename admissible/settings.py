import os

# Django settings for admissible project.

DEBUG = False
TEMPLATE_DEBUG = DEBUG

ADMINS = (
    ('Nicolas Ehrhardt', 'admissible@clubinfo.enpc.fr'),
)

MANAGERS = ADMINS

SITE_ROOT = os.path.abspath(os.path.join(os.path.dirname( __file__ ), '..'))

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql', # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': 'enpcadmis',                      # Or path to database file if using sqlite3.
        'USER': 'enpcadmis',                      # Not used with sqlite3.
        'PASSWORD': 'o78uT4lp9e',                  # Not used with sqlite3.
        'HOST': 'mysql51-21.pro',                      # Set to empty string for localhost. Not used with sqlite3.
        'PORT': '',                      # Set to empty string for default. Not used with sqlite3.
    }
}

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# In a Windows environment this must be set to your system time zone.
TIME_ZONE = 'Europe/Paris'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'fr'

gettext = lambda s: s

LANGUAGES = (
  ('fr', gettext('French')),
)

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# If you set this to False, Django will not format dates, numbers and
# calendars according to the current locale.
USE_L10N = True

# If you set this to False, Django will not use timezone-aware datetimes.
USE_TZ = True

# Absolute filesystem path to the directory that will hold user-uploaded files.
# Example: "/home/media/media.lawrence.com/media/"
MEDIA_ROOT = os.path.join(SITE_ROOT, 'media')

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash.
# Examples: "http://media.lawrence.com/media/", "http://example.com/media/"
MEDIA_URL = '/media/'

# Absolute path to the directory static files should be collected to.
# Don't put anything in this directory yourself; store your static files
# in apps' "static/" subdirectories and in STATICFILES_DIRS.
# Example: "/home/media/media.lawrence.com/static/"
STATIC_ROOT = os.path.abspath(os.path.join(SITE_ROOT, 'static'))

# URL prefix for static files.
# Example: "http://media.lawrence.com/static/"
STATIC_URL = '/static/'

# Additional locations of static files
STATICFILES_DIRS = (
    # ('fiber', os.path.join(SITE_ROOT, 'media')),
    # Put strings here, like "/home/html/static" or "C:/www/django/static".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
)

# List of finder classes that know how to find static files in
# various locations.
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    'compressor.finders.CompressorFinder',
#    'django.contrib.staticfiles.finders.DefaultStorageFinder',
)

# Make this unique, and don't share it with anybody.
SECRET_KEY = '#*9$voths5zbt&amp;huq)^e0u54#=#ip@$5!(4+76ugkha_^xgd!d'

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
#     'django.template.loaders.eggs.Loader',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    # Uncomment the next line for simple clickjacking protection:
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    ## Apps
    # pipeline
    'pipeline.storage.PipelineCachedStorage',
    # fiber
    'fiber.middleware.ObfuscateEmailAddressMiddleware',
    'fiber.middleware.AdminPageMiddleware',
)

ROOT_URLCONF = 'admissible.urls'

# Python dotted path to the WSGI application used by Django's runserver.
WSGI_APPLICATION = 'admissible.wsgi.application'

TEMPLATE_DIRS = (
    os.path.join(os.path.join(os.path.join(SITE_ROOT, 'admissible'), 'templates'), 'fiber'),
    # Put strings here, like "/home/html/django_templates" or "C:/www/django/templates".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
)

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.flatpages',
    ## Apps
    'admissible',
    'userprofile',
    'registration',
    'room',
    'booking',
    # payments
    'paypal.standard.ipn',
    # dev tool
    'pipeline',
    'south',
    # fiber
    'mptt',
    'compressor',
    'fiber',
    # Uncomment the next line to enable the admin:
    'django.contrib.admin',
    # Uncomment the next line to enable admin documentation:
    # 'django.contrib.admindocs',
)

# Installed App variables

# Fiber

FIBER_DEFAULT_TEMPLATE = 'fiber.html'

FIBER_IMAGES_DIR = 'uploads/images'
FIBER_FILES_DIR = 'uploads/files'

import django.conf.global_settings as DEFAULT_SETTINGS

TEMPLATE_CONTEXT_PROCESSORS = DEFAULT_SETTINGS.TEMPLATE_CONTEXT_PROCESSORS + (
    'django.core.context_processors.request',
)

# Paypals

PAYPAL_TEST = True
PAYPAL_IMAGE = "https://www.sandbox.paypal.com/fr_FR/i/btn/btn_buynowCC_LG.gif"
PAYPAL_SANDBOX_IMAGE = "https://www.sandbox.paypal.com/fr_FR/i/btn/btn_buynowCC_LG.gif"
PAYPAL_RECEIVER_EMAIL = "yourpaypalemail@example.com"
PAYPAL_AMOUNT = 25.00
PAYPAL_NOTIFY_URL = ""
#PAYPAL_RETURN_URL = ""
#PAYPAL_CANCEL_URL = ""

# Registration

ACCOUNT_ACTIVATION_DAYS = 7

# Booking

DAYS_TO_PAY = 10

# Emails

EMAIL_USE_TLS = True
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_HOST_USER = 'nico.ehrhardt@gmail.com'
EMAIL_HOST_PASSWORD = '[ouvre-stp-!]886'
EMAIL_CONTACT = 'bonjour@admissible.enpc.org'

# Landing page after login

LOGIN_REDIRECT_URL = '/profile/home'

# Pipeline

PIPELINE_CSS_COMPRESSOR = None

PIPELINE_COMPILERS = (
    'pipeline.compilers.stylus.StylusCompiler',
)

#PIPELINE_STYLUS_BINARY = "/usr/local/bin/stylus -u nib"

STATICFILES_STORAGE = 'pipeline.storage.PipelineStorage'

#PIPELINE = True

PIPELINE_CSS = {
    'core': {
        'source_filenames': (
            'css/style.styl',        
        ),
        'output_filename': 'css/style.css',
        'extra_context': {
            'media': 'screen,projection',
        },
    },
    'bootstrap': {
        'source_filenames': (
            'css/bootstrap.min.css',
        ),
        'output_filename': 'css/bootstrap.min.css',
        'extra_context': {
            'media': 'screen,projection',
        },
    },
}

# A sample logging configuration. The only tangible logging
# performed by this configuration is to send an email to
# the site admins on every HTTP 500 error when DEBUG=False.
# See http://docs.djangoproject.com/en/dev/topics/logging for
# more details on how to customize your logging configuration.

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler'
        }
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
    }
}
