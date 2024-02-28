from django.urls import path
from . import views
from .views import profile_page

urlpatterns = [
    path('profile/', views.profile_page, name='profile_page'),
    path('profile/delete_comment/<int:comment_id>/', views.comment_delete, name='comment_delete'),
    path('post/<int:pk>/edit_post/<int:pk>/', views.post_edit, name='post_edit'),
]