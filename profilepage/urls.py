from django.urls import path
from . import views
from .views import profile_page, profile_comment_delete

urlpatterns = [
    path('profile/', views.profile_page, name='profile_page'),
    path('post/<int:pk>/edit_post/<int:pk>/', views.post_edit, name='post_edit'),
    path('<int:pk>/delete/', views.discussion_delete, name='discussion_delete'),
    path('profile/delete_comment/<int:comment_id>/', views.profile_comment_delete, name='profile_comment_delete'),
]