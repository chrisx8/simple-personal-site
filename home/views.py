from django.shortcuts import render


# csrf failure page
def csrf_failure(request, *args, **argv):
    return render(request, 'csrf_failure.html', status=400)


# 403 error page
def handler403(request, *args, **argv):
    context = {
        'code': 403,
        'title': 'Access Denied',
        'subtitle': 'Sorry, you\'re not permitted to access this page.'
    }
    return render(request, 'error.html', status=context['code'], context=context)


# 404 error page
def handler404(request, *args, **argv):
    context = {
        'code': 404,
        'title': 'Page Not Found',
        'subtitle': 'The page you\'re looking for doesn\'t exist.'
    }
    return render(request, 'error.html', status=context['code'], context=context)


# 500 error page
def handler500(request, *args, **argv):
    context = {
        'code': 500,
        'title': 'Internal Server Error',
        'subtitle': 'Sorry, the server could not process your request right now. Please try again later.'
    }
    return render(request, 'error.html', status=context['code'], context=context)
