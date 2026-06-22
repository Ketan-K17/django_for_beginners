from django.urls import path
from .views import blogpost_list, blogpost_detail

app_name = 'blog'

urlpatterns = [
    path("", blogpost_list, name="home"),
    path("blogpost/<int:pk>/", blogpost_detail, name="blogpost_detail")
    # this <int:pk> thing is a 'path converter'
]