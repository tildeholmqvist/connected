from django.urls import path
from . import views
from .views import profile_page

urlpatterns = [
    path('profile/', views.profile_page, name='profile'),
    path('discussionpost/delete/<int:pk>/', views.discussion_post_delete, name='discussionpost_delete'),
    path('post/edit/<int:pk>/', views.discussionpost_edit, name='discussionpost_edit'),
]