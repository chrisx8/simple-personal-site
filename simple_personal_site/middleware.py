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
class ProxyAuthMiddleware(RemoteUserMiddleware):
	header = settings.REMOTE_USER_HEADER
	email_header = settings.REMOTE_EMAIL_HEADER

	# extend process_request to store user email address
	def process_request(self, request):
		# read username header, skip everything if username doesn't exist
		try:
			username = request.META[self.header]
		except KeyError:
			return

		# read email header, remove email if header doesn't exist or email is invalid
		try:
			email = request.META[self.email_header]
			validate_email(email)
		except (KeyError, ValidationError):
			email = ''

		# update user email
		user = User.objects.get(username=username)
		if user:
			user.email = email
			user.save()

		# pass on login request
		super().process_request(request)
