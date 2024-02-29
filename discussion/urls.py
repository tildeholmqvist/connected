from django.urls import path
from . import views
from .views import DiscussionIndex, create_discussion, discussion_detail, comment_delete

urlpatterns = [
    path('', DiscussionIndex.as_view(), name='discussion_list'),
    path('discussion/', DiscussionIndex.as_view(), name='discussion_index'),
    path("post/<int:pk>/", discussion_detail, name="discussion_detail"),
    path('create_discussion/', create_discussion, name='create_discussion'),
    path('post/<int:pk>/delete_comment/<int:comment_id>/', views.comment_delete, name='comment_delete'),
    path('post/<int:pk>/edit_comment/<int:comment_id>/', views.comment_edit, name='comment_edit'),
]
