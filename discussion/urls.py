from django.urls import path
from . import views
from .views import discussion_list, create_discussion

urlpatterns = [
    path('', views.discussion_list, name='discussion_list'),
    path("post/<int:pk>/", views.discussion_detail, name="discussion_detail"),
    path('category/<str:category>/', views.discussion_category, name='discussion_category'),
    path('create_discussion/', views.create_discussion, name='create_discussion'),
    path('discussion_list/', discussion_list, name='discussion_list'),
]