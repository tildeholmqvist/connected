from django.contrib import admin
from .models import DiscussionPost, DiscussionComment


admin.site.register(DiscussionPost)
admin.site.register(DiscussionComment)


