from django.shortcuts import Http404, HttpResponseRedirect
from .models import ShortURL


# redirect to home when no shorturl is provided
def go_home(request):
    return HttpResponseRedirect('/')


# redirect to desired url
def redirect(request, alias):
    # redirect if url exists
    try:
        url_obj = ShortURL.objects.get(alias=alias)
        assert url_obj.enabled
        return HttpResponseRedirect(url_obj.full_url)
    # 404 if url doesn't exist
    except (AssertionError, ShortURL.DoesNotExist):
        raise Http404(request)
