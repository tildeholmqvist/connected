from django.urls import path
from . import views

urlpatterns = [
    path('', views.discussion_list, name='discussion_list'),
    path("post/<int:pk>/", views.discussion_detail, name="discussion_detail"),
    path('post/new/', views.discussion_create, name='discussion_create'),
]