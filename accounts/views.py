from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views.generic import CreateView

class SignUpView(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy("login")
    # NOTE: Why use reverse_lazy here instead of reverse? The URLs are not loaded when the file is imported for generic class-based views, so we have to use the lazy form of reverse to load them later when they’re available. Basically, if its in a class definition, use reverse_lazy(), anywhere else which gets accessed during request, use reverse()
    template_name = "registration/signup.html"