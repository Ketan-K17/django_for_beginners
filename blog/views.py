from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Blogpost
from django.urls import reverse_lazy

class BlogListView(ListView):
    model = Blogpost
    template_name = "blog/blog.html"
    context_object_name = "blogposts" # optional, it'll default to blogpost_list

class BlogDetailView(DetailView):
    model = Blogpost
    template_name = "blog/blogpost_detail.html"

class BlogCreateView(CreateView):
    model = Blogpost
    template_name = "blog/blogpost_new.html"
    fields = ["title", "author", "body"]

class BlogUpdateView(UpdateView):
    model = Blogpost
    template_name = "blog/blogpost_edit.html"
    fields = ["title", "body"]

class BlogDeleteView(DeleteView):
    model = Blogpost
    template_name = "blog/blogpost_delete.html"
    success_url = reverse_lazy("blog:home")