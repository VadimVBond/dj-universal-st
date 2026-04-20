from django.urls import path
from django.conf import settings
from django.http import HttpResponse
from django.utils.translation import activate
from django_distill import distill_path
from apps.pages.views import home
from apps.gallery.views import placeholder as gallery_home


def get_languages():
    for lang_code, _ in settings.LANGUAGES:
        yield {'lang': lang_code}


def get_default_lang():
    return [None]


def home_wrapper(request, lang=None):
    if lang:
        activate(lang)
    return home(request)


def gallery_wrapper(request, lang=None):
    if lang:
        activate(lang)
    return gallery_home(request)


urlpatterns = [
    # Static pages for each language
    distill_path("<str:lang>/", home_wrapper, name="home", distill_func=get_languages),
    distill_path("<str:lang>/gallery/", gallery_wrapper, name="gallery-index", distill_func=get_languages),
    
    # Root index.html (usually redirects or defaults to EN)
    distill_path("", home_wrapper, name="root-home", distill_func=get_default_lang),
]