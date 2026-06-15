from django.db import models

class Post(models.Model):
    text = models.TextField()

    def __str__(self):
        return self.text[:50] + "..."

# This is our first change to the models file for this 'posts' app. EVERY change to the models file -> eventual change in database schema. This schema is actually stored to the db by a 2 step process. Here's what it looks like - 

# create / change model file -> makemigrations (creates migration file) -> migrate (adopts this schema change in db)

# this 2-step process aka 'activation' of model.