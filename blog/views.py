from django.views.generic import ListView, DetailView
from .models import Blogpost

class BlogListView(ListView):
    model = Blogpost
    template_name = "blog/blog.html"
    context_object_name = "blogposts" # optional, it'll default to blogpost_list

class BlogDetailView(DetailView):
    model = Blogpost
    template_name = "blog/blogpost_detail.html"