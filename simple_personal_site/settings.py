# Django settings for simple_personal_site project.

import secrets
from dotenv import load_dotenv
from os import environ, path

# Generate secret key
key_bytes = 128
SECRET_KEY = secrets.token_urlsafe(key_bytes)

# Build paths inside the project like this: path.join(BASE_DIR, ...)
BASE_DIR = path.dirname(path.dirname(path.abspath(__file__)))

# Load config into system env
# System environment variables ALWAYS TAKES PRECEDENCE
load_dotenv()

try:
    ALLOWED_HOSTS = environ.get('ALLOWED_HOSTS').split(',')
except AttributeError:
    pass

# DEBUG defaults to False.
# SECURITY WARNING: don't run with debug turned on in production!
# Set environment variable DEBUG=TRUE to enable debug
debug_env = environ.get('DEBUG')
if isinstance(debug_env, str) and debug_env.upper() == 'TRUE':
    print('WARNING: Debug mode is enabled!')
    DEBUG = True
    HTML_MINIFY = False
else:
    DEBUG = False
    HTML_MINIFY = True

# Application definition
INSTALLED_APPS = [
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.sitemaps',
    'django.contrib.staticfiles',
    'solo',
    # SPS Apps
    'home.apps.HomeConfig',
    'blog',
    'contact',
    'media',
    'projects',
    'url_shortener.apps.UrlShortenerConfig',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.middleware.gzip.GZipMiddleware',
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

# Database
# Configure DB from env file
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.' + environ.get('DB_TYPE'),
        'NAME': environ.get('DB_NAME'),
        'HOST': environ.get('DB_HOST'),
        'PORT': environ.get('DB_PORT'),
        'USER': environ.get('DB_USERNAME'),
        'PASSWORD': environ.get('DB_PASSWORD'),
    }
}

# Password validation
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]
LOGOUT_REDIRECT_URL = '/'

# Internationalization
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True

# Static files (CSS, JavaScript, Images)
STATIC_URL = '/static/'
MEDIA_URL = '/media/'
STATIC_BASE = path.join(BASE_DIR, 'static_serve')
STATIC_ROOT = path.join(STATIC_BASE, 'static')
MEDIA_ROOT = path.join(STATIC_BASE, 'media')

# Configure SMTP server from env file
try:
    EMAIL_HOST = str(environ.get('EMAIL_HOST'))
    EMAIL_PORT = int(environ.get('EMAIL_PORT'))
    EMAIL_HOST_USER = str(environ.get('EMAIL_HOST_USER'))
    EMAIL_HOST_PASSWORD = str(environ.get('EMAIL_HOST_PASSWORD'))
    if environ.get('EMAIL_USE_TLS').lower() == 'true':
        EMAIL_USE_TLS = True
    elif environ.get('EMAIL_USE_SSL').lower() == 'true':
        EMAIL_USE_SSL = True
    else:
        EMAIL_USE_TLS = False
        EMAIL_USE_SSL = False
except (TypeError, ValueError):
    pass

# Security settings
CSRF_FAILURE_VIEW = 'home.views.csrf_failure'
SESSION_EXPIRE_AT_BROWSER_CLOSE = True
SECURE_BROWSER_XSS_FILTER = True
SECURE_CONTENT_TYPE_NOSNIFF = True
SECURE_REFERRER_POLICY = 'same-origin'
X_FRAME_OPTIONS = 'DENY'

# SSL settings
SITE_SSL = environ.get('SITE_SSL')
if isinstance(SITE_SSL, str) and SITE_SSL.lower() == 'true':
    SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
    CSRF_COOKIE_SECURE = True
    SESSION_COOKIE_SECURE = True

# Site-specific config
ADMIN_URL = environ.get('ADMIN_URL')
STATUS_PAGE_URL = environ.get('STATUS_PAGE_URL')

# Enable admin panel if admin url is set
if ADMIN_URL:
    INSTALLED_APPS.append('django.contrib.admin')
