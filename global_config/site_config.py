from django.conf import settings
from django.db import OperationalError, ProgrammingError

from global_config.models import EmailConfig, ReCaptcha, SiteInfo

try:
	# Load/create db entries, then get object
	site_info = SiteInfo.objects.get_or_create()[0]
	email_conf = EmailConfig.objects.get_or_create()[0]
	recaptcha_conf = ReCaptcha.objects.get_or_create()[0]

	# read config
	SITE_NAME = site_info.site_name
	SITE_PROTOCOL = site_info.site_url.split('://')[0]
	RECAPTCHA_PRIVATE_KEY = recaptcha_conf.private_key
	RECAPTCHA_PUBLIC_KEY = recaptcha_conf.public_key

	# update app settings
	settings.EMAIL_HOST = email_conf.host
	settings.EMAIL_PORT = email_conf.port
	settings.EMAIL_HOST_USER = email_conf.username
	settings.EMAIL_HOST_PASSWORD = email_conf.password
	settings.EMAIL_USE_TLS = email_conf.use_tls
	settings.EMAIL_USE_SSL = email_conf.use_ssl
	settings.RECAPTCHA_PRIVATE_KEY = RECAPTCHA_PRIVATE_KEY
	settings.RECAPTCHA_PUBLIC_KEY = RECAPTCHA_PUBLIC_KEY
except OperationalError or ProgrammingError:
	SITE_NAME, SITE_PROTOCOL, RECAPTCHA_PRIVATE_KEY, RECAPTCHA_PUBLIC_KEY = '', '', '', ''
