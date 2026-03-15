"""Models for blog."""
from __future__ import annotations

from django.db import models
from django.urls import reverse


class Post(models.Model):
    """Blog post."""

    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True)
    excerpt = models.TextField(blank=True)
    content = models.TextField()
    image = models.ImageField(upload_to="blog/", blank=True, null=True)
    published = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self) -> str:
        return self.title

    def get_absolute_url(self) -> str:
        return reverse("blog:detail", kwargs={"slug": self.slug})
