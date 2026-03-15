"""Production settings."""
from __future__ import annotations

import os

from .base import *  # noqa: F403

DEBUG = False

# Comma-separated hosts: "example.com,.example.com"
ALLOWED_HOSTS = [
    host.strip()
    for host in os.getenv("DJANGO_ALLOWED_HOSTS", "").split(",")
    if host.strip()
]