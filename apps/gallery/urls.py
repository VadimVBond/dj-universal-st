"""URL configuration for gallery."""
from __future__ import annotations

from django.urls import path

from . import views

app_name = "gallery"

urlpatterns = [
    path("", views.placeholder, name="index"),
]