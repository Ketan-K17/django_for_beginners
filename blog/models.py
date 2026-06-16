from django.db import models

class Blogpost(models.Model):
    title = models.CharField(max_length=255)
    author = models.ForeignKey(
        "auth.User",
        on_delete=models.CASCADE,
    )
    body = models.TextField()

    # I guess __str__ gets overridden once you come with a custom modelAdmin
    def __str__(self):
        return f"{self.title} - by {self.author}"
   