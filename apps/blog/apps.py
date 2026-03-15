"""Application configuration for blog."""
from __future__ import annotations

from django.apps import AppConfig


class BlogConfig(AppConfig):
    """App config for blog."""

    default_auto_field = "django.db.models.BigAutoField"
    name = "apps.blog"