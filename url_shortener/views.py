from django.shortcuts import Http404, HttpResponseRedirect, HttpResponse
from .models import URL


# redirect to desired url
def redirect(request, alias):
    # redirect if url exists
    try:
        url_obj = URL.objects.get(alias=alias)
        target = url_obj.full_url
    # try 'alias/' if url doesn't exist
    except URL.DoesNotExist:
        # get relative uri
        request_uri = request.META['PATH_INFO'] + request.META['QUERY_STRING']
        # try '<alias/>' if request uri is '<alias>'
        if request_uri.count('/') == 1:
            target = request.build_absolute_uri() + '/'
        # throw 404 otherwise
        else:
            raise Http404
    return HttpResponseRedirect(target)
