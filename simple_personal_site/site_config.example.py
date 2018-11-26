"""
Settings for this site

Rename this file to 'site_config.py' and edit settings accordingly

All fields are REQUIRED, unless otherwise noted
"""

# ------------------------------------------------
# GENERAL SITE CONFIG
# ------------------------------------------------

# Site info
SITE_NAME = 'My Personal Site'
SITE_DESCRIPTION = 'Describe My Personal Site'
SITE_URL = 'https://www.example.com'

# Allowed hostnames
ALLOWED_HOSTS = ['example.com', 'www.example.com']

# Database credentials
# Supported databases: PostgresSQL, MySQL, SQLite
# MySQL URL scheme: mysql://USER:PASSWORD@HOST:PORT/NAME
# Postgres URL scheme: postgres://USER:PASSWORD@HOST:PORT/NAME
# SQLite URL scheme: sqlite:///ABSOLUTE_PATH [OR] sqlite://RELATIVE_PATH
DATABASE_URL = ''

# ReCaptcha credentials
# REQUIRED for forms. Get your ReCaptcha v3 key at https://www.google.com/recaptcha/admin
RECAPTCHA_PRIVATE_KEY = 'your private key'
RECAPTCHA_PUBLIC_KEY = 'your public key'
RECAPTCHA_DEFAULT_ACTION = 'generic'

# Sendgrid API credentials [OPTIONAL]
# NOT REQUIRED. If you don't want to send emails, leave SENDGRID_APIKEY blank
SENDGRID_APIKEY = ''

# ------------------------------------------------
# PROJECTS PAGE PREFERENCES
# ------------------------------------------------

# Number of projects on Projects page
PROJECTS_PER_PAGE = 6

# ------------------------------------------------
# CONTACT PAGE PREFERENCES
# ------------------------------------------------

# Contact email settings
CONTACT_EMAIL = {
    'subject': 'Thanks for contacting me!',
    'from': 'Sender Name <noreply@example.com>',
}