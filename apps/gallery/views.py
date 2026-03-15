"""Views for gallery."""
from __future__ import annotations

from django.http import HttpRequest, HttpResponse


# TODO: Replace this placeholder view with real handlers.
def placeholder(request: HttpRequest) -> HttpResponse:
    """Temporary placeholder response."""

    return HttpResponse("gallery app is ready.")