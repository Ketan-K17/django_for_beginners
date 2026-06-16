from django.shortcuts import render
from .models import Blogpost

def blogpost_list(request):
    posts = Blogpost.objects.all()
    return render(request, "blog/blog.html", {'posts': posts})