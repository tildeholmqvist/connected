from django.db import models
from django.contrib.auth.models import User
from django_summernote.fields import SummernoteTextField


# Model handeling Posts
# Some code is taken from the walkthoughproject "I think therefor I blog"

class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.ManyToManyField("Category", related_name="posts")
    updated_on = models.DateTimeField(auto_now=True)
    excerpt = models.TextField(blank=True)

    class Meta:
        ordering = ["-created_at"]
    
    def __str__(self): 
        return f"{self.title} by {self.author}"

# Model handeling Categories

class Category(models.Model):
    name = models.CharField(max_length=40)

    class Meta:
        verbose_name_plural = "categories"

    def __str__(self):
        return self.name

    
# Model handeling Comments 
# Some code is taken from the walkthoughproject "I think therefor I blog"

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="commenter")
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=False)

    class Meta:
        ordering = ["created_at"]
    
    def __str__(self): 
        return f"{self.body} by {self.author}"
    
    def is_visible_to_user(self, user):
        return self.approved or user == self.author