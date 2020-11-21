# Django settings for simple_personal_site project.

from os import path, environ
import secrets
from dotenv import load_dotenv

# Generate secret key
key_bytes = 128
SECRET_KEY = secrets.token_urlsafe(key_bytes)

# Build paths inside the project like this: path.join(BASE_DIR, ...)
BASE_DIR = path.dirname(path.dirname(path.abspath(__file__)))

# Load config into system env
load_dotenv()

# Configure allowed hosts
ALLOWED_HOSTS = environ.get('ALLOWED_HOSTS').split(',')

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

# Password validators
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]
# Redirect to homepage after login/logout
LOGIN_REDIRECT_URL = '/'
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
STATICFILES_DIRS = [path.join(BASE_DIR, "static")]
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

# OpenID Connect SSO. Only use if explicitly enabled.
USE_OIDC = False
if environ.get('USE_OIDC') == 'True':
    USE_OIDC = True
    # install app
    INSTALLED_APPS.append('mozilla_django_oidc')
    MIDDLEWARE.append('mozilla_django_oidc.middleware.SessionRefresh')
    # Authentication backends. Enable OIDC
    AUTHENTICATION_BACKENDS = (
        'mozilla_django_oidc.auth.OIDCAuthenticationBackend',
        'django.contrib.auth.backends.ModelBackend'
    )
    # configure OIDC from environment variable
    OIDC_USERNAME_ALGO = 'simple_personal_site.context_processor.generate_username'
    OIDC_RP_CLIENT_ID = environ.get('OIDC_RP_CLIENT_ID')
    OIDC_RP_CLIENT_SECRET = environ.get('OIDC_RP_CLIENT_SECRET')
    OIDC_OP_AUTHORIZATION_ENDPOINT = environ.get('OIDC_OP_AUTHORIZATION_ENDPOINT')
    OIDC_OP_JWKS_ENDPOINT = environ.get('OIDC_OP_JWKS_ENDPOINT')
    OIDC_OP_TOKEN_ENDPOINT = environ.get('OIDC_OP_TOKEN_ENDPOINT')
    OIDC_OP_USER_ENDPOINT = environ.get('OIDC_OP_USER_ENDPOINT')
    OIDC_RP_SIGN_ALGO = environ.get('OIDC_RP_SIGN_ALGO')
