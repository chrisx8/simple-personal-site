"""
Django settings for simple_personal_site project.

Generated by 'django-admin startproject' using Django 2.1.3.

For more information on this file, see
https://docs.djangoproject.com/en/2.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.1/ref/settings/
"""

import dj_database_url
import os
import secrets
from django.core.exceptions import ImproperlyConfigured
from dotenv import load_dotenv

# Generate secret key
key_bytes = 128
SECRET_KEY = secrets.token_urlsafe(key_bytes)

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Load config into system env
load_dotenv(dotenv_path=os.path.join(BASE_DIR, 'config.env'))

try:
    ALLOWED_HOSTS = os.environ.get('ALLOWED_HOSTS').split(',')
except AttributeError:
    raise ImproperlyConfigured('ALLOWED_HOSTS is not configured')

# DEBUG defaults to False.
# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False
HTML_MINIFY = True

# Set environment variable DEBUG=TRUE to enable debug
debug_env = os.environ.get('DEBUG')
if isinstance(debug_env, str) and debug_env.upper == 'TRUE':
    DEBUG = True
    HTML_MINIFY = False

# Application definition
INSTALLED_APPS = [
    'whitenoise.runserver_nostatic',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.sitemaps',
    'django.contrib.staticfiles',
    'snowpenguin.django.recaptcha2',
    'solo',
    'blog.apps.BlogConfig',
    'contact.apps.ContactConfig',
    'global_config.apps.GlobalConfigConfig',
    'homepage.apps.HomepageConfig',
    'media.apps.MediaConfig',
    'projects.apps.ProjectsConfig',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.middleware.gzip.GZipMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'htmlmin.middleware.HtmlMinifyMiddleware',
    'htmlmin.middleware.MarkRequestMiddleware',
]

ROOT_URLCONF = 'simple_personal_site.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'simple_personal_site.context_processor.global_tags',
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'simple_personal_site.wsgi.application'

ADMIN_URL = os.environ.get('ADMIN_URL')

# Database
# https://docs.djangoproject.com/en/2.1/ref/settings/#databases

# Configure DB URL from config.env
DATABASE_URL = os.environ.get('DATABASE_URL')
DATABASES = {'default': dj_database_url.config(default=DATABASE_URL)}

# Password validation
# https://docs.djangoproject.com/en/2.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

# Internationalization
# https://docs.djangoproject.com/en/2.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.1/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = 'static'
MEDIA_URL = '/media/'
MEDIA_ROOT = 'media_files'

# Configure SMTP server from config.env
try:
    EMAIL_HOST = str(os.environ.get('EMAIL_HOST'))
    EMAIL_PORT = int(os.environ.get('EMAIL_PORT'))
    EMAIL_HOST_USER = str(os.environ.get('EMAIL_HOST_USER'))
    EMAIL_HOST_PASSWORD = str(os.environ.get('EMAIL_HOST_PASSWORD'))
    if os.environ.get('EMAIL_USE_TLS') == 'True':
        EMAIL_USE_TLS = True
    elif os.environ.get('EMAIL_USE_SSL') == 'True':
        EMAIL_USE_SSL = True
    else:
        EMAIL_USE_TLS = False
        EMAIL_USE_SSL = False
except (TypeError, ValueError):
    pass

# Security settings
NONCE = os.environ.get('NONCE')
SESSION_EXPIRE_AT_BROWSER_CLOSE = True
SECURE_BROWSER_XSS_FILTER = True
SECURE_CONTENT_TYPE_NOSNIFF = True
X_FRAME_OPTIONS = 'DENY'

# ReCaptcha settings
RECAPTCHA_PRIVATE_KEY = str(os.environ.get('RECAPTCHA_PRIVATE_KEY'))
RECAPTCHA_PUBLIC_KEY = str(os.environ.get('RECAPTCHA_PUBLIC_KEY'))
RECAPTCHA_PROXY_HOST = 'https://recaptcha.net'
