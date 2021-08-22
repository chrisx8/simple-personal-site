from django.conf import settings
from django.contrib.auth.models import User
from django.contrib.auth.middleware import RemoteUserMiddleware
from django.core.exceptions import ValidationError
from django.core.validators import validate_email


# Opt out of FLoC
class FLoCOptOutMiddleware:
	def __init__(self, get_response):
		self.get_response = get_response

	def __call__(self, request):
		response = self.get_response(request)
		response['Permissions-Policy'] = 'interest-cohort=()'
		return response


# Use headers or environment variables for SSO
class SPSRemoteUserMiddleware(RemoteUserMiddleware):
	header = settings.REMOTE_USER_HEADER

	# extend process_request to only allow existing user
	def process_request(self, request):
		# read username header and check if user exists
		# skip everything if username doesn't exist
		try:
			username = request.META[self.header]
			user = User.objects.get(username=username)
		except KeyError:
			return

		# continue login request
		super().process_request(request)
