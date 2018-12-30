import datetime
from . import site_config, settings


# global site information
def site_info(request):
    time = datetime.datetime.now()
    context = {
        'SITE_NAME': site_config.SITE_NAME,
        'SITE_DESCRIPTION': site_config.SITE_DESCRIPTION,
        'SITE_URL': site_config.SITE_URL,
        'GA_TRACKING_ID': site_config.GA_TRACKING_ID,
        'HEADER_TITLE': site_config.HEADER_TITLE,
        'HEADER_SUBTITLE': site_config.HEADER_SUBTITLE,
        'FOOTER_COPYRIGHT': site_config.FOOTER_COPYRIGHT,
        'YEAR': time.year,
        'TIMEZONE': settings.TIME_ZONE
    }
    return context
