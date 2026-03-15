"""URL configuration for components."""
from __future__ import annotations

from django.urls import path

from . import views

app_name = "components"

urlpatterns = [
    path("", views.placeholder, name="index"),
]