from django.shortcuts import HttpResponse, render
from blog.models import Article
from projects.models import Project
from simple_personal_site.site_config import MANAGEMENT_URL
from .models import Homepage


# homepage
def home(request):
    try:
        home_obj = Homepage.objects.latest('id')
        latest_articles = Article.objects.order_by('-last_edited', 'title')[:2]
        latest_projects = Project.objects.order_by('-posted', 'title')[:2]
        context = {
            'home': home_obj,
            'latest_articles': latest_articles,
            'latest_projects': latest_projects
        }
        return render(request, 'home.html', context=context)
    except Homepage.DoesNotExist:
        return HttpResponse(f'<h1>Please create a homepage in the <a href="/{MANAGEMENT_URL}">admin portal</a>.<h1>')
