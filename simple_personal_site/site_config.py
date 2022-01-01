from dotenv import load_dotenv
from os import environ

# get site configuration from environment. returns dict with config options
def get_site_config():
	# convert true/false str (case insensitive) to bool
	# "true" (str) = True (bool). everything else = False
	def str_to_bool(input):
		return isinstance(input, str) and input.upper() == 'TRUE'

	# Load config into system env
	# System environment variables ALWAYS TAKES PRECEDENCE
	load_dotenv()

	# ALLOWED_HOST must exist
	assert environ.get('ALLOWED_HOSTS'), "ALLOWED_HOSTS is not configured"

	# build config dict
	config = {
		'DEBUG': str_to_bool(environ.get('DEBUG')),
		'ALLOWED_HOSTS': environ.get('ALLOWED_HOSTS').split(','),
		'SITE_SSL': str_to_bool(environ.get('SITE_SSL')),
		'DB_NAME': environ.get('DB_NAME'),
		'EMAIL_HOST': environ.get('EMAIL_HOST'),
		'EMAIL_PORT': environ.get('EMAIL_PORT'),
		'EMAIL_HOST_USER': environ.get('EMAIL_HOST_USER'),
    	'EMAIL_HOST_PASSWORD': environ.get('EMAIL_HOST_PASSWORD'),
		'EMAIL_USE_TLS': str_to_bool(environ.get('EMAIL_USE_TLS')),
		'EMAIL_USE_SSL': str_to_bool(environ.get('EMAIL_USE_SSL')),
		'ADMIN_URL': environ.get('ADMIN_URL'),
		'REVERSE_PROXY_AUTH': str_to_bool(environ.get('REVERSE_PROXY_AUTH')),
		'REMOTE_USER_HEADER': environ.get('REMOTE_USER_HEADER'),
	}

	return config
