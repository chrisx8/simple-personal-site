from django.shortcuts import HttpResponse, render

from .models import Homepage


# homepage
def home(request):
    try:
        home_obj = Homepage.objects.latest('id')
        featured_articles = home_obj.featured_articles.order_by('-last_edited')
        featured_projects = home_obj.featured_projects.filter(show=True)
        context = {
            'home': home_obj,
            'featured_articles': featured_articles,
            'featured_projects': featured_projects
        }
        return render(request, 'home.html', context=context)
    except Homepage.DoesNotExist:
        return HttpResponse('<h1>Please create a homepage in the <a href="/manage/">admin portal</a>.<h1>')
