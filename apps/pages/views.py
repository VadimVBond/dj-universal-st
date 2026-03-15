"""Views for pages."""
from __future__ import annotations

from django.http import HttpRequest, HttpResponse
from django.shortcuts import render


def home(request: HttpRequest) -> HttpResponse:
    """Render the landing page."""

    # Static gallery data for the home page filterable grid.
    gallery_categories = ["UI", "Website", "Dashboard", "Landing"]
    gallery_items = [
        {
            "title": "Tailwind UI Kit",
            "image": "images/tailwind1.png",
            "category": "UI",
            "description": "Component kit for fast UI builds.",
        },
        {
            "title": "DaisyUI Elements",
            "image": "images/daisyui1.png",
            "category": "UI",
            "description": "Clean, lightweight interface pieces.",
        },
        {
            "title": "Bootstrap Landing",
            "image": "images/bootstrap1.png",
            "category": "Landing",
            "description": "Landing layout with CTA blocks.",
        },
        {
            "title": "Preline Landing",
            "image": "images/preline1.png",
            "category": "Landing",
            "description": "Modern hero and feature sections.",
        },
        {
            "title": "Flowbite Website",
            "image": "images/flowbite1.png",
            "category": "Website",
            "description": "Multi-section website layout.",
        },
        {
            "title": "Preline Website",
            "image": "images/preline2.png",
            "category": "Website",
            "description": "Navigation-focused site structure.",
        },
        {
            "title": "Dashboard Overview",
            "image": "images/tailwind2.png",
            "category": "Dashboard",
            "description": "Metrics and charts overview.",
        },
        {
            "title": "DaisyUI Dashboard",
            "image": "images/daisyui2.png",
            "category": "Dashboard",
            "description": "Cards and panels for analytics.",
        },
    ]

    context = {
        "gallery_categories": gallery_categories,
        "gallery_items": gallery_items,
    }
    return render(request, "pages/home.html", context)
