from django.urls import path
from . import views

urlpatterns = [
    path('', views.BlogList.as_view(), name='home'),
    path('templates/about/', views.about, name='about'),
    path("post/<int:pk>/", views.blog_detail, name="blog_detail"),
    path("category/<category>/", views.blog_category, name="blog_category"),

]