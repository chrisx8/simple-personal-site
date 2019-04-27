from django.contrib import admin
from solo.admin import SingletonModelAdmin
from .models import Homepage

admin.site.register(Homepage, SingletonModelAdmin)
