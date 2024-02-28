from django.db import models
from django.contrib.auth.models import User

# Create your models here.

#https://www.devhandbook.com/django/user-profile/

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(max_length=500, blank=True)
    def __str__(self):
        return f'{self.user.username} Profile'