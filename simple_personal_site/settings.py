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
from dotenv import load_dotenv

# Generate secret key
key_bytes = 128
SECRET_KEY = secrets.token_urlsafe(key_bytes)

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Load config into system env
load_dotenv(dotenv_path=os.path.join(BASE_DIR, 'site_config.env'))
env_vars = os.environ

ALLOWED_HOSTS = env_vars['ALLOWED_HOSTS'].split(',')
DATABASE_URL = env_vars['DATABASE_URL']
ADMIN_URL = env_vars['ADMIN_URL']
NONCE = env_vars['NONCE']

# DEBUG defaults to False.
# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

# Set environment variable DEBUG=True to enable debug
if os.environ.get('DEBUG') == 'True':
    DEBUG = True

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
    'captcha',
    'solo',
    'blog.apps.BlogConfig',
    'contact.apps.ContactConfig',
    'global_config.apps.GlobalConfigConfig',
    'homepage.apps.HomepageConfig',
    'media.apps.MediaConfig',
    'projects.apps.ProjectsConfig',
    'shorturl.apps.ShorturlConfig',
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

HTML_MINIFY = True

# Database
# https://docs.djangoproject.com/en/2.1/ref/settings/#databases

# Configure DB URL from site_config
DATABASES = {'default': dj_database_url.config(default=DATABASE_URL)}

# Password validation
# https://docs.djangoproject.com/en/2.1/ref/settings/#auth-password-validators

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
MEDIA_URL = '/uploads/'
MEDIA_ROOT = 'uploads'

# Security settings
SESSION_EXPIRE_AT_BROWSER_CLOSE = True
SECURE_BROWSER_XSS_FILTER = True
SECURE_CONTENT_TYPE_NOSNIFF = True
X_FRAME_OPTIONS = 'DENY'

# Captcha settings
CAPTCHA_FOREGROUND_COLOR = '#001600'
CAPTCHA_LETTER_ROTATION = (-25, 25)
