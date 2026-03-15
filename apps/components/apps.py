"""Application configuration for components."""
from __future__ import annotations

from django.apps import AppConfig


class ComponentsConfig(AppConfig):
    """App config for components."""

    default_auto_field = "django.db.models.BigAutoField"
    name = "apps.components"