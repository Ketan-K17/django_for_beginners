from django.shortcuts import render
from django.views.generic import TemplateView

def home_page_view(request):
    context = {
        "inventory_list": ["Widget 1", "Widget 2", "Widget 3"],
        "greeting": "THAnk you FOR visitING.",
    }
    return render(request, "home.html", context)


# NOTE: There's 3 ways of writing views today in Django, 1. function-based: what we've been doing so far, 2. Class-based, 3. Generic Class-based (technically a subset of class-based views). This one is generic class-based. I think the difference between latter 2 is that in Generic Class-based views come with built-in methods for common tasks like rendering a template, handling HTTP requests, and more.
class AboutPageView(TemplateView):
    template_name = "about.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["contact_address"] = "Kalika Square"
        context["phone_number"] = "555-555-5555"
        return context

    # NOTE: One of the most powerful, useful, and commonly used methods in Django is get_context_data(). It is the recommended approach for updating the template's context in a generic class-based view. 