from django.shortcuts import render
from .models import Project

# all projects
def projects(request):
    all_projects = Project.objects.all()
    context = {
        'projects': all_projects,
    }
    return render(request, 'projects.html', context=context)
