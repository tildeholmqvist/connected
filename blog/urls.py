from django.urls import path
from . import views

urlpatterns = [
    path('', views.BlogList.as_view(), name='home'),
    path('about/', views.about, name='about'),
    path("post/<slug:slug>/", views.blog_detail, name="blog_detail"),
    path("category/<category>/", views.blog_category, name="blog_category"),
    path('post/<slug:slug>/edit_comment/<int:comment_id>/', views.comment_edit, name='comment_edit'),
    path('post/<slug:slug>/delete_comment/<int:comment_id>/', views.comment_delete, name='comment_delete'),
]