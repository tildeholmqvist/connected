from django.contrib import admin
from .models import Category, Post, Comment
from django_summernote.admin import SummernoteModelAdmin

# This code is from the walkthorugh project "I think therefor I blog"
@admin.register(Post)
class PostAdmin(SummernoteModelAdmin):
    search_fields = ['title', 'content']
    summernote_fields = ('content',)

# Register your models here.
admin.site.register(Category)
admin.site.register(Comment)

