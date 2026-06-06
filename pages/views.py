# A view is a Python function that accepts a Web request and returns a Web response. 

from django.http import HttpResponse
from django.shortcuts import render

def home_page_view(request):
    return HttpResponse("HomePage")

def about_page_view(request):
    return render(request, "pages/about.html", context={})
    # NOTE: Templates often have some dynamic content (not HTML) that is to be shown on the final rendered HTML. These could include values picked from a database or other sources. All of these values to be shown on the final rendered HTML must be passed to the template as 'context' data. 'context' is a dictionary of key-value pairs that are used to pass data to the template. You use it as the last of 3 params to pass to the render() function..

    # so a render function needs 1. httprequest obj, 2. template name, 3. context data