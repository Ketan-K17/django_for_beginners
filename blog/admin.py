from django.contrib import admin
from .models import Blogpost

class PostAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "author",
        "body",
    )
admin.site.register(Blogpost, PostAdmin)
