# A view is a Python function that accepts a Web request and returns a Web response. 

# pages/views.py
from django.http import HttpResponse

def home_page_view(request):
    return HttpResponse("Hello, World!")