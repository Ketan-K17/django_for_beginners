"""
URL configuration for django_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.views.generic.base import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path("accounts/", include("django.contrib.auth.urls")),
    # heading into accounts uses the 'auth' app, which comes off the box.. you can then use the login / logout functionality in it.
    path("accounts/", include("accounts.urls")), # it's important this signup url comes below login url pattern... Since it's read top-down, if the top login url fails, then we do signup.
    path('', include('pages.urls')),
    path('posts/', include('posts.urls')),
    path('blog/', include('blog.urls')),
    path('newspaper_app/', include('newspaper_app.urls')),

]
