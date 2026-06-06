# pages/urls.py
from django.urls import path
from .views import home_page_view, AboutPageView

urlpatterns = [
    path("", home_page_view, name="home"), # ALWAYS name your urls.. This way you don't need to hardcode path everywhere... if url changes tomorrow for some reason, only place to edit would be urls.py file.
    path("about/", AboutPageView.as_view(), name="about"),
]