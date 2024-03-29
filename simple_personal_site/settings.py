# Django settings for simple_personal_site project.

import secrets
from os import path

import pymysql

from .site_config import get_site_config

# Generate secret key
key_bytes = 128
SECRET_KEY = secrets.token_urlsafe(key_bytes)

# Build paths inside the project like this: path.join(BASE_DIR, ...)
BASE_DIR = path.dirname(path.dirname(path.abspath(__file__)))

# read config from environment
config = get_site_config()

# 400 if request Host is not in ALLOWED_HOSTS
ALLOWED_HOSTS = config["ALLOWED_HOSTS"]

# DEBUG defaults to False. Set environment variable DEBUG=TRUE to enable debug
# SECURITY WARNING: don't run with debug turned on in production!
if config["DEBUG"]:
    print("\033[93m\033[1m" + "WARNING: Debug mode is enabled!" + "\033[0m")
    DEBUG = True
    HTML_MINIFY = False
else:
    DEBUG = False
    HTML_MINIFY = True

# Application definition
INSTALLED_APPS = [
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sitemaps",
    "django.contrib.staticfiles",
    "solo",
    # SPS Apps
    "home.apps.HomeConfig",
    "blog.apps.BlogConfig",
    "contact.apps.ContactConfig",
    "media.apps.MediaConfig",
    "projects.apps.ProjectsConfig",
    "url_shortener.apps.UrlShortenerConfig",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.middleware.gzip.GZipMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    "htmlmin.middleware.HtmlMinifyMiddleware",
    "htmlmin.middleware.MarkRequestMiddleware",
]

ROOT_URLCONF = "simple_personal_site.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "simple_personal_site.context_processor.global_tags",
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "simple_personal_site.wsgi.application"

# Database
DEFAULT_AUTO_FIELD = "django.db.models.AutoField"
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends." + config["DB_TYPE"],
        "NAME": config["DB_NAME"],
        "HOST": config["DB_HOST"],
        "PORT": config["DB_PORT"],
        "USER": config["DB_USERNAME"],
        "PASSWORD": config["DB_PASSWORD"],
    }
}

pymysql.install_as_MySQLdb()

# Password validation
AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator"
    },
    {"NAME": "django.contrib.auth.password_validation.MinimumLengthValidator"},
    {"NAME": "django.contrib.auth.password_validation.CommonPasswordValidator"},
    {"NAME": "django.contrib.auth.password_validation.NumericPasswordValidator"},
]

# Internationalization
LANGUAGE_CODE = "en-us"
TIME_ZONE = "UTC"
USE_I18N = False
USE_TZ = True

# Static files (CSS, JavaScript, Images)
STATIC_URL = "/static/"
MEDIA_URL = "/media/"
STATIC_BASE = path.join(BASE_DIR, "static_serve")
STATIC_ROOT = path.join(STATIC_BASE, "static")
MEDIA_ROOT = path.join(STATIC_BASE, "media")

# SMTP server for email
EMAIL_HOST = config["EMAIL_HOST"]
EMAIL_PORT = config["EMAIL_PORT"]
EMAIL_HOST_USER = config["EMAIL_HOST_USER"]
EMAIL_HOST_PASSWORD = config["EMAIL_HOST_PASSWORD"]
EMAIL_USE_TLS = config["EMAIL_USE_TLS"]
EMAIL_USE_SSL = config["EMAIL_USE_SSL"]

# Cookie settings
CSRF_COOKIE_SAMESITE = "Strict"
SESSION_COOKIE_SAMESITE = "Strict"

# Security settings
LOGOUT_REDIRECT_URL = "/"
CSRF_FAILURE_VIEW = "home.views.csrf_failure"
SESSION_EXPIRE_AT_BROWSER_CLOSE = True
SECURE_BROWSER_XSS_FILTER = True
SECURE_CONTENT_TYPE_NOSNIFF = True
SECURE_REFERRER_POLICY = "same-origin"
X_FRAME_OPTIONS = "DENY"

# SSL settings
SITE_SSL = config["SITE_SSL"]
if SITE_SSL:
    SECURE_PROXY_SSL_HEADER = ("HTTP_X_FORWARDED_PROTO", "https")
    CSRF_COOKIE_SECURE = True
    SESSION_COOKIE_SECURE = True

# Site-specific options
ADMIN_URL = config["ADMIN_URL"]
STATUS_PAGE_URL = config["STATUS_PAGE_URL"]
BLOG_ARTICLES_PER_PAGE = 10
PROJECTS_PER_PAGE = 6

# Enable admin panel if admin url is set
if ADMIN_URL:
    ADD_APPS = [
        "django.contrib.sessions",
        "django.contrib.messages",
        "django.contrib.admin",
    ]
    ADD_MIDDLEWARE = [
        "django.contrib.sessions.middleware.SessionMiddleware",
        "django.contrib.messages.middleware.MessageMiddleware",
        "django.contrib.auth.middleware.AuthenticationMiddleware",
    ]
    INSTALLED_APPS.extend(ADD_APPS)
    MIDDLEWARE.extend(ADD_MIDDLEWARE)

# Use REMOTE_USER header for authentication
REMOTE_USER_HEADER = config["REMOTE_USER_HEADER"]
if ADMIN_URL and config["REVERSE_PROXY_AUTH"]:
    AUTHENTICATION_BACKENDS = ["django.contrib.auth.backends.RemoteUserBackend"]
    MIDDLEWARE.append("simple_personal_site.middleware.SPSRemoteUserMiddleware")
