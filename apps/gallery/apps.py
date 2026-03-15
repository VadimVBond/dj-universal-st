"""Application configuration for gallery."""
from __future__ import annotations

from django.apps import AppConfig


class GalleryConfig(AppConfig):
    """App config for gallery."""

    default_auto_field = "django.db.models.BigAutoField"
    name = "apps.gallery"