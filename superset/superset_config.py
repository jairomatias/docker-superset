import json
import os

# ---------------------------------------------------------
# Caravel specific config
# ---------------------------------------------------------
ROW_LIMIT = int(os.getenv("ROW_LIMIT", 50000))
WEBSERVER_THREADS = int(os.getenv("WEBSERVER_THREADS", 8))
SUPERSET_WORKERS = int(os.getenv("SUPERSET_WORKERS", 24))

SUPERSET_WEBSERVER_PORT = int(os.getenv("SUPERSET_WEBSERVER_PORT", 8088))
# ---------------------------------------------------------

# ---------------------------------------------------------
# Flask App Builder configuration
# ---------------------------------------------------------
# Your App secret key
SECRET_KEY = os.getenv("SECRET_KEY", "\2\1thisismyscretkey\1\2\e\y\y\h")

# The SQLAlchemy connection string.
SQLALCHEMY_DATABASE_URI = os.getenv(
    "SQLALCHEMY_DATABASE_URI",
    "sqlite:////home/superset/.superset/superset.db")

# Flask-WTF flag for CSRF
CSRF_ENABLED = os.getenv("CSRF_ENABLED", "1") in ("True", "true", "1")

# Set this API key to enable Mapbox visualizations
MAPBOX_API_KEY = os.getenv("MAPBOX_API_KEY", "")

# Whether to run the web server in debug mode or not
DEBUG = os.getenv("DEBUG", "0") in ("True", "true", "1")

try:
    CACHE_CONFIG = json.loads(os.getenv("CACHE_CONFIG", "{}"))
except ValueError:
    CACHE_CONFIG = {}

AUTH_TYPE = int(os.getenv("AUTH_TYPE", 1))
AUTH_LDAP_SERVER = os.getenv("AUTH_LDAP_SERVER")
AUTH_LDAP_BIND_USER = os.getenv("AUTH_LDAP_BIND_USER")
AUTH_LDAP_BIND_PASSWORD = os.getenv("AUTH_LDAP_BIND_PASSWORD")
AUTH_LDAP_SEARCH = os.getenv("AUTH_LDAP_SEARCH")
AUTH_LDAP_UID_FIELD = os.getenv("AUTH_LDAP_UID_FIELD")

AUTH_USER_REGISTRATION = os.getenv("AUTH_USER_REGISTRATION", "0") in ("True", "true", "1")
AUTH_USER_REGISTRATION_ROLE = os.getenv("AUTH_USER_REGISTRATION_ROLE")
