from django.db import models
from django.contrib.auth.models import User

# Model handeling Categories

class Category(models.Model):
    name = models.CharField(max_length=40)


# Model handeling Posts
# Some code is taken from the walkthoughproject "I think therefor I blog"

class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    categories = models.ManyToManyField("Category", related_name="posts")
    updated_on = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-created_on"]
    
    def __str__(self): 
        return f"{self.title} by {self.author}"
    

# Model handeling Comments 
# Some code is taken from the walkthoughproject "I think therefor I blog"

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    apporoved = models.BooleanField(default=False)

    class Meta:
        ordering = ["created_at"]
    
    def __str__(self): 
        return f"{self.body} by {self.author}"