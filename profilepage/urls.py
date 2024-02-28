from django.urls import path
from . import views
from .views import profile_page, delete_comment

urlpatterns = [
    path('profile/', views.profile_page, name='profile_page'),
    path('profile/<slug:slug>/delete_post/<int:post_id>/', views.delete_post, name='post_delete'),
    path('post/<int:pk>/edit_post/<int:pk>/', views.post_edit, name='post_edit'),
]