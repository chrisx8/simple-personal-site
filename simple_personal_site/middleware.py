from django.conf import settings
from django.contrib.auth.middleware import RemoteUserMiddleware


# Override header in built-in RemoteUserMiddleware
class SPSRemoteUserMiddleware(RemoteUserMiddleware):
    header = settings.REMOTE_USER_HEADER
