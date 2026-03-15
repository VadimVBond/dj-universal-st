"""WSGI config for the project."""
from __future__ import annotations

import os

from django.core.wsgi import get_wsgi_application

# Default to dev settings for local runserver.
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings.dev")

application = get_wsgi_application()