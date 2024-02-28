from django.urls import path
from . import views
from .views import profile_page

urlpatterns = [
    path('profile/', views.profile_page, name='profile'),
]