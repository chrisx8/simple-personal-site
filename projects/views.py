from django.core.paginator import Paginator
from django.http import HttpResponseRedirect
from django.shortcuts import render, reverse
from .models import Project, ProjectsConfig


# all projects
def projects(request):
    projects_config = ProjectsConfig.objects.get_or_create()[0]
    # exclude hidden projects
    all_projects = Project.objects.order_by('order')
    paginator = Paginator(all_projects, projects_config.projects_per_page)
    # get page numbers as url param. Default to page 1
    page = request.GET.get('page')
    if page is None:
        page = 1
    # go to page 1 if invalid
    try:
        page = int(page)
        assert(1 <= page <= paginator.num_pages)
    except (AssertionError, ValueError):
        return HttpResponseRedirect(reverse('projects'))
    projects_on_page = paginator.get_page(page)
    # one page number before/after current
    if int(page)-2 >= 0:
        display_page_range = paginator.page_range[int(page)-2:int(page)+1]
    else:
        display_page_range = paginator.page_range[:int(page)+1]
    context = {
        'projects': projects_on_page,
        'page_range': display_page_range,
    }
    return render(request, 'projects.html', context=context)
