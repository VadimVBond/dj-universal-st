"""Views for blog."""
from __future__ import annotations

from django.http import HttpRequest, HttpResponse
from django.shortcuts import get_object_or_404, render

from .models import Post


def index(request: HttpRequest) -> HttpResponse:
    """Render blog list page."""

    posts = Post.objects.filter(published=True).order_by("-created_at")
    context = {"posts": posts}
    return render(request, "blog/list.html", context)


def detail(request: HttpRequest, slug: str) -> HttpResponse:
    """Render a single blog post page."""

    post = get_object_or_404(Post, slug=slug, published=True)
    context = {"post": post}
    return render(request, "blog/article.html", context)
