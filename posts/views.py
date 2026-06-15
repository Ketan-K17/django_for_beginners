# from django.shortcuts import render
# from .models import Post
# from django.urls import reverse

# def post_list(request):
#     posts = Post.objects.all()
#     return render(request, "posts.html", {"posts": posts})

from django.views.generic import ListView
from .models import Post

class PostList(ListView):
    model = Post
    template_name = "posts.html"