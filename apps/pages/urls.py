"""URL configuration for pages."""
from __future__ import annotations

from django.urls import path
from django.views.generic import TemplateView

from . import views

app_name = "pages"

urlpatterns = [
    path("", views.home, name="home"),
    path("ui/bootstrap/", TemplateView.as_view(template_name="ui/bootstrap.html"), name="ui-bootstrap"),
    path("ui/tailwind/", TemplateView.as_view(template_name="ui/tailwind.html"), name="ui-tailwind"),
    path("ui/flowbite/", TemplateView.as_view(template_name="ui/flowbite.html"), name="ui-flowbite"),
    path("ui/daisyui/", TemplateView.as_view(template_name="ui/daisyui.html"), name="ui-daisyui"),
    path("ui/preline/", TemplateView.as_view(template_name="ui/preline.html"), name="ui-preline"),
]