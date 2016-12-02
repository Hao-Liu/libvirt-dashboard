"""
Django settings for caselink project.

Generated by 'django-admin startproject' using Django 1.8.7.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.8/ref/settings/
"""

from __future__ import absolute_import

from celery.schedules import crontab

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.8/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'lo*_kgg$k%47$#mc6cr*3!3^9buv6c_*2l3$w0lqg1=0(_=eo='

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'crispy_forms',
    'bootstrapform',
    'rest_framework',
    'caselink',
    'djcelery',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.security.SecurityMiddleware',
)

ROOT_URLCONF = 'caselink.urls'

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
                'caselink.utils.settings_inject.settings_inject',
            ],
        },
    },
]

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
        },
    },
    'loggers': {
        'django': {
            'handlers': ['console'],
            'level': os.getenv('DJANGO_LOG_LEVEL', 'INFO'),
        },
    },
}

WSGI_APPLICATION = 'caselink.wsgi.application'


CELERYBEAT_SCHEDULE = {
    # crontab(hour=0, minute=0, day_of_week='saturday')
    'schedule-name': {
        'task': 'caselink.tasks.common.test_task',
        'schedule': crontab(hour='*/1', day_of_week='mon,tue,wed,thu,fri')
    },
}

# Database
# https://docs.djangoproject.com/en/1.8/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': '',
        'USER': '',
        'PASSWORD': '',
        'HOST': 'localhost',
        'PORT': '',
    }
}


# Internationalization
# https://docs.djangoproject.com/en/1.8/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.8/howto/static-files/

STATIC_URL = '/static/'

FIXTURE_DIRS = [
    'caselink/fixture/'
]

REST_FRAMEWORK = {
    'DEFAULT_FILTER_BACKENDS': ('rest_framework.filters.DjangoFilterBackend',),
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.LimitOffsetPagination',
    'PAGE_SIZE': 100,
}

CASELINK = {
}

CASELINK_MAITAI = {
    'USER': '',
    'PASSWORD': '',
    'ENABLE': False,
    'REASON': 'Maitai haven\'t implemented the workflow we needed yet.',
    'DEFAULT_ASSIGNEE': '',
    'PARENT_ISSUE': '',

    'SERVER': '',
    'DEPLOYMENT': '',
    'CASEADD_DEFINITION': '',
    'CASEUPDATE_DEFINITION': '',
}

CASELINK_POLARION = {
    # 'URL': URL is in pylarion
    'ENABLE': False,
    # Parameters for Polarion workitem fetching
    'PROJECT': '',
    'SPACES': [],
    'REASON': 'Polarion support is disabled for now, please contract the admin.',
    'URL': '',
}

CASELINK_JIRA = {
    # 'URL': URL is in pylarion
    'ENABLE': False,
    'USER': '',
    # Parameters for Polarion workitem fetching
    'PASSWORD': '',
    'SERVER': '',
    'PARENT_ISSUE': '',
}

CASELINK_MEMBERS = ('member1 member2')
CASELINK_DEFAULT_ASSIGNEE = 'member1'

try:
    from caselink.settings_instance import *
except ImportError:
    print("Instance setting not found.")
