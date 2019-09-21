from django.conf import settings
from django.db.utils import OperationalError, ProgrammingError
from global_config.models import SiteInfo

try:
	# Load/create db entries, then get object
	site_info = SiteInfo.objects.get_or_create()[0]

	# read config
	SITE_NAME = site_info.site_name
	SITE_PROTOCOL = site_info.site_url.split('://')[0]
except (OperationalError, ProgrammingError):
	SITE_NAME, SITE_PROTOCOL = '', ''
