# core/context_processors.py

from . import config

def global_config(request):
    return {
        "config": config,
        # request.ui устанавливается в UIMiddleware
        "ui": getattr(request, "ui", config.UI_DEFAULT),
    }