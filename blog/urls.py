from django.urls import path
from .views import BlogListView, BlogDetailView

app_name = 'blog'

urlpatterns = [
    path("", BlogListView.as_view(), name="home"),
    path("blogpost/<int:pk>/", BlogDetailView.as_view(), name="blogpost_detail")
    # this <int:pk> thing is a 'path converter'
]