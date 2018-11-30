from django.shortcuts import Http404, HttpResponseRedirect
from .models import ShortURL


# redirect to home when no shorturl is provided
def go_home(request):
    return HttpResponseRedirect('/')


# redirect to desired url
def redirect(request, alias):
    # redirect if url exists
    try:
        full_url = ShortURL.objects.get(alias=alias).full_url
        return HttpResponseRedirect(full_url)
    # 404 if url doesn't exist
    except:
        raise Http404(request)
