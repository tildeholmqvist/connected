from django.urls import path
from . import views
from .views import profile_page
from blog.views import comment_delete

urlpatterns = [
    path('profile/', views.profile_page, name='profile_page'),
    path('profile/<int:comment_id>/delete_comment/<int:comment_id>/', comment_delete, name='delete_comment'),
    path('post/<int:pk>/edit_post/<int:pk>/', views.post_edit, name='post_edit'),
    path('profile/<int:pk>/edit_comment/<int:comment_id>/', views.comment_edit, name='comment_edit'),
]