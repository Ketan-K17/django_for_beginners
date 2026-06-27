from django.conf import settings
from django.db import models
from django.urls import reverse

class Blogpost(models.Model):
    title = models.CharField(max_length=255)
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )
    body = models.TextField()

    # I guess __str__ gets overridden once you come with a custom modelAdmin
    def __str__(self):
        return f"{self.title} - by {self.author}"

    def get_absolute_url(self):
        return reverse("blog:blogpost_detail", kwargs={"pk": self.pk})
   