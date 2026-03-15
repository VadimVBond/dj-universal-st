"""Application configuration for pages."""
from __future__ import annotations

from django.apps import AppConfig


class PagesConfig(AppConfig):
    """App config for pages."""

    default_auto_field = "django.db.models.BigAutoField"
    name = "apps.pages"