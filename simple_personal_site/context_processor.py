import datetime
from contact.models import SocialMediaLink
from . import site_config


# global site information
def site_info(request):
    time = datetime.datetime.now()
    social_links = SocialMediaLink.objects.order_by('platform')
    context = {
        'SITE_NAME': site_config.SITE_NAME,
        'SITE_DESCRIPTION': site_config.SITE_DESCRIPTION,
        'SITE_URL': site_config.SITE_URL,
        'GA_TRACKING_ID': site_config.GA_TRACKING_ID,
        'FATHOM_URL': site_config.FATHOM_URL,
        'FATHOM_SITE_ID': site_config.FATHOM_SITE_ID,
        'HEADER_TITLE': site_config.HEADER_TITLE,
        'HEADER_SUBTITLE': site_config.HEADER_SUBTITLE,
        'FOOTER_COPYRIGHT': site_config.FOOTER_COPYRIGHT,
        'YEAR': time.year,
        'social_links': social_links,
    }
    return context
