import os
from dotenv import load_dotenv

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Load config into system env
load_dotenv(dotenv_path=os.path.join(BASE_DIR, 'site_config.env'))
env_vars = os.environ

# Assign env to variables
SITE_NAME = env_vars['SITE_NAME']
SITE_DESCRIPTION = env_vars['SITE_DESCRIPTION']
SITE_URL = env_vars['SITE_URL']
ALLOWED_HOSTS = env_vars['ALLOWED_HOSTS'].split(',')
SECRET_KEY = env_vars['SECRET_KEY']
DATABASE_URL = env_vars['DATABASE_URL']
RECAPTCHA_PRIVATE_KEY = env_vars['RECAPTCHA_PRIVATE_KEY']
RECAPTCHA_PUBLIC_KEY = env_vars['RECAPTCHA_PUBLIC_KEY']
GA_TRACKING_ID = env_vars['GA_TRACKING_ID']
EMAIL_HOST = env_vars['EMAIL_HOST']
EMAIL_PORT = int(env_vars['EMAIL_PORT'])
EMAIL_HOST_USER = env_vars['EMAIL_HOST_USER']
EMAIL_HOST_PASSWORD = env_vars['EMAIL_HOST_PASSWORD']
EMAIL_USE_TLS = env_vars['EMAIL_USE_TLS'] == 'True'
EMAIL_USE_SSL = env_vars['EMAIL_USE_SSL'] == 'True'
HEADER_TITLE = env_vars['HEADER_TITLE']
HEADER_SUBTITLE = env_vars['HEADER_SUBTITLE']
FOOTER_COPYRIGHT = env_vars['FOOTER_COPYRIGHT']
ARTICLES_PER_PAGE = int(env_vars['ARTICLES_PER_PAGE'])
PROJECTS_PER_PAGE = int(env_vars['PROJECTS_PER_PAGE'])
CONTACT_EMAIL = {
    'subject': env_vars['CONTACT_EMAIL_SUBJECT'],
    'from': env_vars['CONTACT_EMAIL_FROM'],
}