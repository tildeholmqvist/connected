from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class DiscussionPost(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    category = models.ManyToManyField("Category", related_name="discussion")
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    updated_on = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-created_at"]
    
    def __str__(self): 
        return f"{self.title} by {self.author}"



class Category(models.Model):
    name = models.CharField(max_length=40)

    class Meta:
        verbose_name_plural = "categories"

    def __str__(self):
        return self.name