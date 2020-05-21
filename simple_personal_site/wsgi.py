# WSGI config for simple_personal_site project.

import os
from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'simple_personal_site.settings')

application = get_wsgi_application()
