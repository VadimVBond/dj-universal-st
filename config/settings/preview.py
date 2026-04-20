from .base import *

ROOT_URLCONF = "config.urls_preview"

INSTALLED_APPS += ["django_distill"]

STATIC_ROOT = BASE_DIR / "static_distill_temp"
DISTILL_DIR = BASE_DIR / "dist"

DEBUG = False
ALLOWED_HOSTS = ["*"]