from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class DiscussionPost(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    updated_on = models.DateTimeField(auto_now=True)
    approved = models.BooleanField(default=False)

    class Meta:
        ordering = ["-created_at"]
    
    def __str__(self): 
        return f"{self.title} by {self.author}"


class DiscussionComment(models.Model):
    post = models.ForeignKey(DiscussionPost, on_delete=models.CASCADE, related_name='comments')
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="discussion_comments")
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=False)

    class Meta:
        ordering = ["created_at"]
    
    def __str__(self): 
        return f"{self.body} by {self.author}"
    
    def is_visible_to_user(self, user):
        return self.approved or user == self.author