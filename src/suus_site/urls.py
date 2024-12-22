from django.urls import path

from .views import (
    HOME_PAGE_NAME,
    HomePage,
)

site_urlpatterns = [
    path("", HomePage.as_view(), name=HOME_PAGE_NAME),
]