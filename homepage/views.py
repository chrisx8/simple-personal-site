from django.shortcuts import render

from .models import Homepage


# homepage
def home(request):
    home_obj = Homepage.objects.latest('id')
    context = {
        'home': home_obj
    }
    return render(request, 'home.html', context=context)
