"""URL configuration for the project."""
from __future__ import annotations

from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path
from django.views.i18n import set_language

urlpatterns = [
    path("i18n/setlang/", set_language, name="set_language"),
    path("", include("apps.pages.urls")),
    path("blog/", include("apps.blog.urls")),
    path("admin/", admin.site.urls),
]

# Serve media files in development.
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


