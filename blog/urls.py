from django.urls import path
from .views import BlogListView, BlogDetailView, BlogCreateView, BlogUpdateView, BlogDeleteView

app_name = 'blog'

urlpatterns = [
    path("", BlogListView.as_view(), name="home"),
    path("blogpost/<int:pk>/", BlogDetailView.as_view(), name="blogpost_detail"),
    # this <int:pk> thing is a 'path converter'
    path("blogpost/new/", BlogCreateView.as_view(), name="blogpost_new"),
    path("blogpost/<int:pk>/edit/", BlogUpdateView.as_view(), name="blogpost_edit"),
    path("blogpost/<int:pk>/delete/", BlogDeleteView.as_view(), name="blogpost_delete")
]