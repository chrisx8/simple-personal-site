from django.conf import settings
from django.contrib.auth.middleware import RemoteUserMiddleware


# Opt out of FLoC
class FLoCOptOutMiddleware:
	def __init__(self, get_response):
		self.get_response = get_response
	
	def __call__(self, request):
		response = self.get_response(request)
		response['Permissions-Policy'] = 'interest-cohort=()'
		return response


# Use headers or environment variables for SSO
class HeaderAuthMiddleware(RemoteUserMiddleware):
	header = settings.REMOTE_USER_HEADER
	# TODO: read user email address
