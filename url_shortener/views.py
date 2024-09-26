from django.shortcuts import Http404, HttpResponseRedirect

from .models import URL


# redirect to desired url
def redirect(request, alias):
    # redirect if url exists
    try:
        url_obj = URL.objects.get(alias=alias)
        return HttpResponseRedirect(url_obj.full_url)
    # 404 if not
    except URL.DoesNotExist:
        raise Http404
