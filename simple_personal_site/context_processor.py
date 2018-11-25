from .site_config import SITE_NAME, SITE_DESCRIPTION, SITE_URL

def site_info(request):
    # global site information
    return {'SITE_NAME': SITE_NAME, 'SITE_DESCRIPTION': SITE_DESCRIPTION, 'SITE_URL': SITE_URL}