from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Profile
from blog.models import Category
from discussion.models import DiscussionPost

# Create your views here.

@login_required
def profile_page(request):
    user_profile = Profile.objects.get(user=request.user)
    bio = user_profile.bio
    categories = Category.objects.all() 
    discussion_posts = DiscussionPost.objects.filter(author=request.user)

    context = {
        "categories": categories,
        'bio': user_profile.bio,
        "profile": user_profile,
        "discussion_posts": discussion_posts,
    }
    return render(request, 'profilepage/profile.html', context)