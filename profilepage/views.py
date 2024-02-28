from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Profile
from blog.models import Category

# Create your views here.

@login_required
def profile_page(request):
    user_profile = Profile.objects.get(user=request.user)
    categories = Category.objects.all() 
    context = {
        "categories": categories,
        "profile": user_profile,
    }
    return render(request, 'profilepage/profile.html', context)