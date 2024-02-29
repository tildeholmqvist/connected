from django.urls import path
from . import views
from .views import profile_page

urlpatterns = [
    path('profile/', views.profile_page, name='profile_page'),
    path('post/<int:pk>/edit_post/<int:pk>/', views.post_edit, name='post_edit'),
    path('profile/<int:pk>/edit_comment/<int:comment_id>/', views.comment_edit, name='comment_edit'),
    path('profile/delete_comment/<int:comment_id>/', views.comment_delete_discussion , name='delete_comment_discussion'),
]