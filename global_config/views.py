from django.shortcuts import render


def csrf_failure(request):
    return render(request, 'error/csrf_failure.html')


# 404 error page
def handler404(request, *args, **argv):
    return render(request, 'error/404.html', status=404)


# 500 error page
def handler500(request, *args, **argv):
    return render(request, 'error/500.html', status=500)
