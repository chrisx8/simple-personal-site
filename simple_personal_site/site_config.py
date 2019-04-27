from django.conf import settings
from django.db import OperationalError
from global_config.models import EmailConfig, ReCaptcha, SiteInfo

BLOG_DESCRIPTION = ''
PROJECTS_DESCRIPTION = ''
ARTICLES_PER_PAGE = 2
PROJECTS_PER_PAGE = 2

# Load site info from DB
try:
    site_info = SiteInfo.objects.get()
    SITE_NAME = site_info.site_name
    SITE_PROTOCOL = site_info.site_url.split('://')[0]
except SiteInfo.DoesNotExist:
    SITE_NAME = 'Simple Personal Site'
    SITE_PROTOCOL = 'http'

# Load email config from DB
try:
    email_conf = EmailConfig.objects.get()
    settings.EMAIL_HOST = email_conf.host
    settings.EMAIL_PORT = email_conf.port
    settings.EMAIL_HOST_USER = email_conf.username
    settings.EMAIL_HOST_PASSWORD = email_conf.password
    settings.EMAIL_USE_TLS = email_conf.use_tls
    settings.EMAIL_USE_SSL = email_conf.use_ssl
except (OperationalError, EmailConfig.DoesNotExist):
    pass

# Load ReCaptcha config from DB
try:
    recaptcha_conf = ReCaptcha.objects.get()
    RECAPTCHA_PRIVATE_KEY = recaptcha_conf.private_key
    RECAPTCHA_PUBLIC_KEY = recaptcha_conf.public_key
except (OperationalError, ReCaptcha.DoesNotExist):
    RECAPTCHA_PRIVATE_KEY = None
    RECAPTCHA_PUBLIC_KEY = None

settings.RECAPTCHA_PRIVATE_KEY = RECAPTCHA_PRIVATE_KEY
settings.RECAPTCHA_PUBLIC_KEY = RECAPTCHA_PUBLIC_KEY
