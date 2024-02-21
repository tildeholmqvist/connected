from django.urls import path
from . import views
from .views import create_discussion, discussion_detail, discussion_category

urlpatterns = [
    path('', views.discussion_list, name='discussion_list'),
    path("post/<int:pk>/", discussion_detail, name="discussion_detail"),
    path('category/<str:category>/', discussion_category, name='discussion_category'),
    path('create_discussion/', create_discussion, name='create_discussion'),
]