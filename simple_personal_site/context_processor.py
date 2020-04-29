from datetime import datetime
from home.models import SiteInfo, SocialMediaLink


# global site information
def global_tags(request):
    # query db
    site_info = SiteInfo.objects.get_or_create()[0]
    social_links = SocialMediaLink.objects.order_by('platform')
    # build context
    time = datetime.now()
    context = {
        'SITE_NAME': site_info.site_name,
        'SITE_DESCRIPTION': site_info.description,
        'SITE_URL': site_info.site_url,
        'HEADER_TITLE': site_info.header_title,
        'HEADER_SUBTITLE': site_info.header_subtitle,
        'FOOTER_COPYRIGHT': site_info.footer_copyright,
        'YEAR': time.year,
        'social_links': social_links
    }
    return context
