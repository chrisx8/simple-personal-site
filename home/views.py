from django.conf import settings
from django.shortcuts import render, HttpResponseRedirect, Http404
from blog.models import Article
from projects.models import Project
from .models import Homepage


def home(request):
    try:
        home_obj = Homepage.objects.get()
    # no homepage object if homepage doesn't exist
    except Homepage.DoesNotExist:
        home_obj = None
    # get latest projects and articles
    latest_articles = Article.objects.order_by('-last_edited', 'title')[:2]
    latest_projects = Project.objects.order_by('order')[:2]
    # go to setup if homepage is empty
    if not home_obj and not latest_articles and not latest_projects:
        context = {'admin_url': settings.ADMIN_URL}
        return render(request, 'setup.html', context=context)
    # render homepage
    context = {
        'home': home_obj,
        'latest_articles': latest_articles,
        'latest_projects': latest_projects
    }
    return render(request, 'home.html', context=context)


def skip_setup(request):
    # get/create homepage
    result = Homepage.objects.get_or_create()
    # 404 if object isn't created
    if not result[1]:
        raise Http404
    # redirect if object is created
    return HttpResponseRedirect('/')


# create SOCIAL_LINKS override for error pages
def create_status_link():
    # skip if status page url is not set
    if not settings.STATUS_PAGE_URL:
        return None

    # override to show status page link
    class StatusPageLink():
        url = settings.STATUS_PAGE_URL
        platform = 'System Status'
    return [StatusPageLink()]


# csrf failure page
def csrf_failure(request, *args, **argv):
    context = {'SOCIAL_LINKS': create_status_link()}
    return render(request, 'csrf_failure.html', status=400, context=context)


# 403 error page
def handler403(request, *args, **argv):
    context = {
        'SOCIAL_LINKS': create_status_link(),
        'code': 403,
        'title': 'Access Denied',
        'subtitle': 'Sorry, you\'re not permitted to access this page.'
    }
    return render(request, 'error.html', status=context['code'], context=context)


# 404 error page
def handler404(request, *args, **argv):
    context = {
        'SOCIAL_LINKS': create_status_link(),
        'code': 404,
        'title': 'Page Not Found',
        'subtitle': 'The page you\'re looking for doesn\'t exist.'
    }
    return render(request, 'error.html', status=context['code'], context=context)


# 500 error page
def handler500(request, *args, **argv):
    context = {
        'SOCIAL_LINKS': create_status_link(),
        'code': 500,
        'title': 'Internal Server Error',
        'subtitle': 'Sorry, the server could not process your request right now. Please try again later.'
    }
    return render(request, 'error.html', status=context['code'], context=context)
