from os import environ

from dotenv import load_dotenv


# get site configuration from environment. returns dict with config options
def get_site_config():
    # convert true/false str (case insensitive) to bool
    # "true" (str) = True (bool). everything else = False
    def str_to_bool(input):
        return isinstance(input, str) and input.upper() == "TRUE"

    # Load config into system env
    # System environment variables ALWAYS TAKES PRECEDENCE
    load_dotenv()

    # ALLOWED_HOST must exist
    assert environ.get("ALLOWED_HOSTS"), "ALLOWED_HOSTS is not configured"
    # DB_TYPE must be 'sqlite3', 'mysql', or 'postgresql'
    SUPPORTED_DB = set(("sqlite3", "mysql", "postgresql"))
    assert environ.get("DB_TYPE") in SUPPORTED_DB, (
        f"DB_TYPE must be one of {SUPPORTED_DB}"
    )

    # build config dict
    config = {
        "DEBUG": str_to_bool(environ.get("DEBUG")),
        "ALLOWED_HOSTS": environ.get("ALLOWED_HOSTS").split(","),
        "SITE_SSL": str_to_bool(environ.get("SITE_SSL")),
        "DB_TYPE": environ.get("DB_TYPE"),
        "DB_NAME": environ.get("DB_NAME"),
        "DB_HOST": environ.get("DB_HOST"),
        "DB_PORT": environ.get("DB_PORT"),
        "DB_USERNAME": environ.get("DB_USERNAME"),
        "DB_PASSWORD": environ.get("DB_PASSWORD"),
        "EMAIL_HOST": environ.get("EMAIL_HOST"),
        "EMAIL_PORT": environ.get("EMAIL_PORT"),
        "EMAIL_HOST_USER": environ.get("EMAIL_HOST_USER"),
        "EMAIL_HOST_PASSWORD": environ.get("EMAIL_HOST_PASSWORD"),
        "EMAIL_USE_TLS": str_to_bool(environ.get("EMAIL_USE_TLS")),
        "EMAIL_USE_SSL": str_to_bool(environ.get("EMAIL_USE_SSL")),
        "ADMIN_URL": environ.get("ADMIN_URL"),
        "REVERSE_PROXY_AUTH": str_to_bool(environ.get("REVERSE_PROXY_AUTH")),
        "REMOTE_USER_HEADER": environ.get("REMOTE_USER_HEADER"),
        "STATUS_PAGE_URL": environ.get("STATUS_PAGE_URL"),
    }

    return config
