import os
from .base import *

DEBUG = True
SECRET_KEY = os.getenv("SECRET_KEY")
ALLOWED_HOSTS = ["127.0.0.1"]

# Databases
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}

# CSRF
CSRF_TRUSTED_ORIGINS = ["http://localhost:8001"]
