from django.http import HttpResponseRedirect, Http404
from django.shortcuts import render
from blog.models import Article
from projects.models import Project
from simple_personal_site.settings import ADMIN_URL
from .models import Homepage


def home(request):
    try:
        home_obj = Homepage.objects.get()
    # no homepage object if homepage doesn't exist
    except Homepage.DoesNotExist:
        home_obj = None
    # get latest projects and articles
    latest_articles = Article.objects.order_by('-last_edited', 'title')[:2]
    latest_projects = Project.objects.order_by('-posted', 'title')[:2]
    if not home_obj and not len(latest_articles) and not len(latest_projects):
        # go to setup if homepage is empty
        context = {'admin_url': ADMIN_URL}
        return render(request, 'setup.html', context=context)
    elif not home_obj:
        # no homepage object if homepage doesn't exist
        context = {
            'latest_articles': latest_articles,
            'latest_projects': latest_projects
        }
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


def nav_noscript(request):
    return render(request, 'nav_noscript.html')
