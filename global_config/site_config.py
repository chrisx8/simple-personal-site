from django.conf import settings
from django.db.utils import OperationalError, ProgrammingError
from global_config.models import EmailConfig, SiteInfo

try:
	# Load/create db entries, then get object
	site_info = SiteInfo.objects.get_or_create()[0]
	email_conf = EmailConfig.objects.get_or_create()[0]

	# read config
	SITE_NAME = site_info.site_name
	SITE_PROTOCOL = site_info.site_url.split('://')[0]

	# update app settings
	settings.EMAIL_HOST = email_conf.host
	settings.EMAIL_PORT = email_conf.port
	settings.EMAIL_HOST_USER = email_conf.username
	settings.EMAIL_HOST_PASSWORD = email_conf.password
	settings.EMAIL_USE_TLS = email_conf.use_tls
	settings.EMAIL_USE_SSL = email_conf.use_ssl
except (OperationalError, ProgrammingError):
	SITE_NAME, SITE_PROTOCOL = '', ''
