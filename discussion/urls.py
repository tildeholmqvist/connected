from django.urls import path
from . import views
from .views import DiscussionIndex, create_discussion, discussion_detail, discussion_category

urlpatterns = [
    path('', DiscussionIndex.as_view(), name='discussion_list'),
    path('discussion/', DiscussionIndex.as_view(), name='discussion_index'),
    path("post/<int:pk>/", discussion_detail, name="discussion_detail"),
    path('category/<str:category>/', discussion_category, name='discussion_category'),
    path('create_discussion/', create_discussion, name='create_discussion'),
]