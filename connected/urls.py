"""
URL configuration for connected project.
"""

from django.contrib import admin
from django.urls import path
from django.urls import include
from profilepage import views as profilepage_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('profile/', profilepage_views.profile_page, name='profile'),
    path("accounts/", include("allauth.urls")),
    path('summernote/', include('django_summernote.urls')),
    path("", include("blog.urls")),
    path('discussion/', include('discussion.urls')),
]
