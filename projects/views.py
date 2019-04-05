from django.core.paginator import Paginator
from django.http import HttpResponseRedirect
from django.shortcuts import render, reverse
from simple_personal_site.site_config import PROJECTS_PER_PAGE, PROJECTS_DESCRIPTION
from .models import Project


# all projects
def projects(request):
    # exclude hidden projects
    all_projects = Project.objects.filter(show=True).order_by('title')
    paginator = Paginator(all_projects, PROJECTS_PER_PAGE)
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
        'SITE_DESCRIPTION': PROJECTS_DESCRIPTION
    }
    return render(request, 'projects.html', context=context)
