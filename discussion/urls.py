from django.urls import path
from . import views
from .views import DiscussionIndex, create_discussion, discussion_detail, comment_delete, discussion_delete, discussion_edit

urlpatterns = [
    path('', views.DiscussionIndex.as_view(), name='discussion_list'),
    path('discussion/', views.DiscussionIndex.as_view(), name='discussion_index'),
    path("post/<int:pk>/", views.discussion_detail, name="discussion_detail"),
    path('create_discussion/', views.create_discussion, name='create_discussion'),
    path('post/<int:pk>/delete_comment/<int:comment_id>/', views.comment_delete, name='comment_delete'),
    path('discussion/post/<int:pk>/edit_comment/<int:comment_id>/', views.comment_edit, name='comment_edit'),
    path('<int:pk>/delete/', views.discussion_delete, name='discussion_delete'),
    path('discussion/edit/<int:pk>/', views.discussion_edit, name='discussion_edit'),
]