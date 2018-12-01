from .site_config import SITE_NAME, SITE_DESCRIPTION, SITE_URL, HEADER_SUBTITLE, HEADER_TITLE


# global site information
def site_info(request):
    context = {
        'SITE_NAME': SITE_NAME,
        'SITE_DESCRIPTION': SITE_DESCRIPTION,
        'SITE_URL': SITE_URL,
        'HEADER_TITLE': HEADER_TITLE,
        'HEADER_SUBTITLE': HEADER_SUBTITLE
    }
    return context
