from django.shortcuts import Http404, HttpResponseRedirect
from .models import URL


# redirect to home when no url is provided
def go_home(request):
    return HttpResponseRedirect('/')


# redirect to desired url
def redirect(request, alias):
    # redirect if url exists
    try:
        url_obj = URL.objects.get(alias=alias)
        return HttpResponseRedirect(url_obj.full_url)
    # 404 if url doesn't exist
    except URL.DoesNotExist:
        raise Http404(request)
