from django.contrib import admin
from .models import Category, Post, Comment
from django_summernote.admin import SummernoteModelAdmin

# This code is from the walkthorugh project "I think therefor I blog"
@admin.register(Post)
class PostAdmin(SummernoteModelAdmin):
    list_display = ('title', 'author', 'created_at', 'updated_on',)
    list_filter = ('categories', 'created_at')

# Register your models here.
admin.site.register(Comment)
admin.site.register(Category)