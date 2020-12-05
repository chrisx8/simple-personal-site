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
    if not home_obj and not len(latest_articles) and not len(latest_projects):
        # go to setup if homepage is empty
        context = {'admin_url': settings.ADMIN_URL}
        return render(request, 'setup.html', context=context)
    else:
        context = {
            'home': home_obj,
            'latest_articles': latest_articles,
            'latest_projects': latest_projects
        }
    return render(request, 'home.html', context=context)


def skip_setup(request):
    # get/create homepage
    result = Homepage.objects.get_or_create()
    # redirect if object created, 404 otherwise
    if result[1]:
        return HttpResponseRedirect('/')
    else:
        raise Http404


# create context dict for error pages
def create_error_page_context():
    # skip if status page url is not set
    if not settings.STATUS_PAGE_URL:
        return {'social_links': []}

    # override social links to show status page link
    class StatusPageLink():
        url = settings.STATUS_PAGE_URL
        platform = 'System Status'
    context = {'social_links': [StatusPageLink()]}
    return context


# csrf failure page
def csrf_failure(request, *args, **argv):
    return render(request, 'error/csrf_failure.html', status=403, context=create_error_page_context())


# 403 error page
def handler403(request, *args, **argv):
    return render(request, 'error/403.html', status=403, context=create_error_page_context())


# 404 error page
def handler404(request, *args, **argv):
    return render(request, 'error/404.html', status=404, context=create_error_page_context())


# 500 error page
def handler500(request, *args, **argv):
    return render(request, 'error/500.html', status=500, context=create_error_page_context())
