from django.urls import path
from .views import blogpost_list

urlpatterns = [
    path("", blogpost_list, name="home"),
]