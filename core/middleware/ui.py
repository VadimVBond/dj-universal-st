# core/middleware/ui.py

from django.utils.deprecation import MiddlewareMixin
from core import config

class UIMiddleware:
    """
    Устанавливает request.ui из cookie или GET-параметра ?ui=...
    Если пришёл GET-param, сохраняет его в cookie в ответе.
    """
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # priority: ?ui=... -> cookie -> default
        q_ui = request.GET.get("ui")
        cookie_ui = request.COOKIES.get("ui")
        if q_ui and q_ui in config.UI_AVAILABLE:
            request.ui = q_ui
            request._ui_set_via_query = True
        elif cookie_ui and cookie_ui in config.UI_AVAILABLE:
            request.ui = cookie_ui
        else:
            request.ui = config.UI_DEFAULT

        response = self.get_response(request)

        if getattr(request, "_ui_set_via_query", False):
            response.set_cookie("ui", request.ui, max_age=60*60*24*365, samesite="Lax")
        return response