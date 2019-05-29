from django.http import HttpResponseRedirect, Http404
from django.shortcuts import render
from blog.models import Article
from projects.models import Project
from simple_personal_site.settings import ADMIN_URL
from .models import Homepage


def home(request):
    # get latest projects and articles
    latest_articles = Article.objects.order_by('-last_edited', 'title')[:2]
    latest_projects = Project.objects.order_by('-posted', 'title')[:2]
    try:
        home_obj = Homepage.objects.get()
        assert len(latest_articles) and len(latest_projects)
        context = {
            'home': home_obj,
            'latest_articles': latest_articles,
            'latest_projects': latest_projects
        }
    except Homepage.DoesNotExist and AssertionError:
        # go to setup if homepage is empty
        context = {'admin_url': ADMIN_URL}
        return render(request, 'setup.html', context=context)
    # no homepage object if homepage doesn't exist
    except Homepage.DoesNotExist:
        context = {
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
