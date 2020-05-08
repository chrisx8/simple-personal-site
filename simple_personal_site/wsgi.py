# WSGI config for simple_personal_site project.

import os
from django.core.wsgi import get_wsgi_application
from whitenoise import WhiteNoise
from simple_personal_site.settings import STATIC_ROOT, STATIC_URL, MEDIA_ROOT, MEDIA_URL

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'simple_personal_site.settings')

application = get_wsgi_application()

# serve static with whitenoise
application = WhiteNoise(application, root=STATIC_ROOT)
application.add_files(MEDIA_ROOT, prefix=MEDIA_URL)
