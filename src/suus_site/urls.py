from django.urls import path

from .views import (
    GET_LLM_RESPONSE_FOR_SUUS_NAME,
    HOME_PAGE_NAME,
    GetLLMResponseForSuus,
    HomePage,
)

site_urlpatterns = [
    path("", HomePage.as_view(), name=HOME_PAGE_NAME),
    path(
        "get-llm-response-for-suus/",
        GetLLMResponseForSuus.as_view(),
        name=GET_LLM_RESPONSE_FOR_SUUS_NAME,
    ),
]