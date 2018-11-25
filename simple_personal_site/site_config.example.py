"""
Settings for this site

Rename this file to 'site_config.py' and edit settings accordingly
"""

# Site name
SITE_NAME = 'My Personal Site'

# Allowed hostnames
ALLOWED_HOSTS = ['example.com', 'www.example.com']

# Database credentials
# Supported databases: PostgresSQL, MySQL, SQLite
# MySQL URL scheme: mysql://USER:PASSWORD@HOST:PORT/NAME
# Postgres URL scheme: postgres://USER:PASSWORD@HOST:PORT/NAME
# SQLite URL scheme: sqlite:///ABSOLUTE_PATH [OR] sqlite://RELATIVE_PATH
DATABASE_URL = ''

# contact email settings
SENDGRID_APIKEY = ''
CONTACT_EMAIL = {
    'subject': 'Thanks for contacting me!',
    'from': 'Name <noreply@example.com>',
}