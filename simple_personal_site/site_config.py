import os

from django.db import OperationalError
from dotenv import load_dotenv
from global_config.models import EmailConfig, ReCaptcha

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Load config into system env
load_dotenv(dotenv_path=os.path.join(BASE_DIR, 'site_config.env'))
env_vars = os.environ

# Assign env to variables
SITE_NAME = env_vars['SITE_NAME']
SITE_DESCRIPTION = env_vars['SITE_DESCRIPTION']
SITE_URL = env_vars['SITE_URL']
SITE_PROTOCOL = SITE_URL.split('://')[0]


BLOG_DESCRIPTION = env_vars['BLOG_DESCRIPTION']
PROJECTS_DESCRIPTION = env_vars['PROJECTS_DESCRIPTION']
ARTICLES_PER_PAGE = int(env_vars['ARTICLES_PER_PAGE'])
PROJECTS_PER_PAGE = int(env_vars['PROJECTS_PER_PAGE'])


# Load email config from DB
try:
    email_conf = EmailConfig.objects.get()
    EMAIL_HOST = email_conf.host
    EMAIL_PORT = email_conf.port
    EMAIL_HOST_USER = email_conf.username
    EMAIL_HOST_PASSWORD = email_conf.password
    EMAIL_USE_TLS = email_conf.use_tls
    EMAIL_USE_SSL = email_conf.use_ssl
except (OperationalError, EmailConfig.DoesNotExist):
    EMAIL_HOST = None
    EMAIL_PORT = None
    EMAIL_HOST_USER = None
    EMAIL_HOST_PASSWORD = None
    EMAIL_USE_TLS = None
    EMAIL_USE_SSL = None

# Load ReCaptcha config from DB
try:
    recaptcha_conf = ReCaptcha.objects.get()
    RECAPTCHA_PRIVATE_KEY = recaptcha_conf.private_key
    RECAPTCHA_PUBLIC_KEY = recaptcha_conf.public_key
except (OperationalError, ReCaptcha.DoesNotExist):
    RECAPTCHA_PRIVATE_KEY = None
    RECAPTCHA_PUBLIC_KEY = None
