from django.contrib import admin
from .models import Category
from .models import DiscussionPost, DiscussionComment


admin.site.register(Category)
admin.site.register(DiscussionPost)
admin.site.register(DiscussionComment)

# Register your models here.
