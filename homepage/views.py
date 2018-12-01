from django.shortcuts import HttpResponse, render

from .models import Homepage


# homepage
def home(request):
    try:
        home_obj = Homepage.objects.latest('id')
        context = {'home': home_obj}
        return render(request, 'home.html', context=context)
    except:
        return HttpResponse('<h1>Please create a homepage in the <a href="/admin/">management portal</a>.<h1>')
