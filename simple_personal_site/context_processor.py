import datetime
from global_config.models import SocialMediaLink
from global_config.models import Fathom, GoogleAnalytics, SiteInfo


# global site information
def global_tags(request):
    context = {}
    try:
        fathom = Fathom.objects.get()
        context.update({'FATHOM_URL': fathom.fathom_url, 'FATHOM_SITE_ID': fathom.site_id})
    except Fathom.DoesNotExist:
        pass
    try:
        google_analytics = GoogleAnalytics.objects.get()
        context.update({'GA_TRACKING_ID': google_analytics.ga_tracking_id})
    except GoogleAnalytics.DoesNotExist:
        pass
    try:
        site_info = SiteInfo.objects.get()
        site_info_dict = {
            'SITE_NAME': site_info.site_name,
            'SITE_DESCRIPTION': site_info.description,
            'SITE_URL': site_info.site_url,
            'HEADER_TITLE': site_info.header_title,
            'HEADER_SUBTITLE': site_info.header_subtitle,
            'FOOTER_COPYRIGHT': site_info.footer_copyright
        }
        context.update(site_info_dict)
    except SiteInfo.DoesNotExist:
        pass
    social_links = SocialMediaLink.objects.order_by('platform')
    time = datetime.datetime.now()
    context.update({

        'YEAR': time.year,
        'social_links': social_links,
    })
    return context
