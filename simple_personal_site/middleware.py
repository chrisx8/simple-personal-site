from django.conf import settings


# Opt out of FLoC
class FLoCOptOutMiddleware:
	def __init__(self, get_response):
		self.get_response = get_response

	def __call__(self, request):
		response = self.get_response(request)
		response['Permissions-Policy'] = 'interest-cohort=()'
		return response


# Override header in built-in RemoteUserMiddleware
class SPSRemoteUserMiddleware(RemoteUserMiddleware):
	header = settings.REMOTE_USER_HEADER
