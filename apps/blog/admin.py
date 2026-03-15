"""Admin configuration for blog."""
from __future__ import annotations

from django.contrib import admin

from .models import Post


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    """Admin configuration for blog posts."""

    pass
