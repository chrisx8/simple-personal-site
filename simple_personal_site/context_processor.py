import datetime
from global_config.models import Fathom, GoogleAnalytics, SiteInfo, SocialMediaLink
from simple_personal_site.settings import NONCE


# global site information
def global_tags(request):
    # query db
    fathom = Fathom.objects.get_or_create()[0]
    google_analytics = GoogleAnalytics.objects.get_or_create()[0]
    site_info = SiteInfo.objects.get_or_create()[0]
    social_links = SocialMediaLink.objects.order_by('platform')
    # build context
    time = datetime.datetime.now()
    context = {
        'FATHOM_URL': fathom.fathom_url,
        'FATHOM_SITE_ID': fathom.site_id,
        'GA_TRACKING_ID': google_analytics.ga_tracking_id,
        'SITE_NAME': site_info.site_name,
        'SITE_DESCRIPTION': site_info.description,
        'SITE_URL': site_info.site_url,
        'HEADER_TITLE': site_info.header_title,
        'HEADER_SUBTITLE': site_info.header_subtitle,
        'FOOTER_COPYRIGHT': site_info.footer_copyright,
        'YEAR': time.year,
        'social_links': social_links
    }
    if NONCE:
        context['NONCE'] = NONCE
    return context
