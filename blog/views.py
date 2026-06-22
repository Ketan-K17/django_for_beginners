from django.shortcuts import render, get_object_or_404
from .models import Blogpost

def blogpost_list(request):
    posts = Blogpost.objects.all()
    return render(request, "blog/blog.html", {'posts': posts})

def blogpost_detail(request, pk):
    # get_object_or_404 queries db for object, and returns 404 if nothing found.
    blogpost = get_object_or_404(Blogpost, pk=pk)
    return render(request, "blog/blogpost_detail.html", {"blogpost": blogpost})