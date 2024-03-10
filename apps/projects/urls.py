from django.urls import path 

from .views import WebPageView


urlpatterns = [
    path("", WebPageView.as_view(), name="web-page")
]
