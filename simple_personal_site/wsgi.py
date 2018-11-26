"""
WSGI config for simple_personal_site project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/2.1/howto/deployment/wsgi/
"""

import os

from whitenoise import WhiteNoise
from django.core.wsgi import get_wsgi_application
from simple_personal_site.settings import BASE_DIR

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'simple_personal_site.settings')

application = get_wsgi_application()

# serve static with whitenoise
application = WhiteNoise(application, root=os.path.join(BASE_DIR, 'static'))
application.add_files(os.path.join(BASE_DIR, 'uploads'), prefix='uploads/')
