from django.contrib.auth.models import AbstractUser
from django.db import models

# you use the AbstractUser class to create your custom user model, outside of the default user model that django comes with. AbstractUser is identical to User in fields, except that you can add new fields to AbstractUser. 

# we'll use AbstractUser in this tutorial atleast, but another popular approach is to maintain a separate 'UserProfile' class and keep a one-to-one field in the original User model to map each instance of the User model to an instance of the UserProfile model..
class CustomUser(AbstractUser):
    age = models.PositiveIntegerField(null=True, blank=True)