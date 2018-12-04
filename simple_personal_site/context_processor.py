import datetime
from .site_config import SITE_NAME, SITE_DESCRIPTION, SITE_URL, HEADER_SUBTITLE, HEADER_TITLE, FOOTER_COPYRIGHT


# global site information
def site_info(request):
    time = datetime.datetime.now()
    context = {
        'SITE_NAME': SITE_NAME,
        'SITE_DESCRIPTION': SITE_DESCRIPTION,
        'SITE_URL': SITE_URL,
        'HEADER_TITLE': HEADER_TITLE,
        'HEADER_SUBTITLE': HEADER_SUBTITLE,
        'FOOTER_COPYRIGHT': FOOTER_COPYRIGHT,
        'YEAR': time.year,
    }
    return context
