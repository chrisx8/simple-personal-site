from django.core.paginator import Paginator
from django.http import HttpResponseRedirect
from django.shortcuts import render, reverse
from .models import Project, ProjectsConfig


# all projects
def projects(request):
    try:
        # get projects config
        projects_config = ProjectsConfig.objects.get()
    except ProjectsConfig.DoesNotExist:
        # create blog config with defaults
        projects_config = ProjectsConfig()
        projects_config.save()
    # exclude hidden projects
    all_projects = Project.objects.order_by('-posted', 'title')
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
    if projects_config.description:
        description = projects_config.description
        context['SITE_DESCRIPTION'] = description
    return render(request, 'projects.html', context=context)
