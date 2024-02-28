from django.shortcuts import render, get_object_or_404, HttpResponseRedirect, reverse
from django.shortcuts import render
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Profile
from blog.models import Category
from discussion.models import DiscussionPost
from discussion.forms import DiscussionPostForm 

@login_required
def profile_page(request):
    user_profile = Profile.objects.get(user=request.user)
    categories = Category.objects.all() 
    discussions = DiscussionPost.objects.filter(author=request.user)

    context = {
        "categories": categories,
        "bio": user_profile.bio,
        "profile": user_profile,
        "discussions": discussions,
    }

    return render(request, 'profilepage/profile.html', context)

@login_required
def post_edit(request, post_id):
    post = get_object_or_404(DiscussionPost, pk=post_id, author=request.user)
    if request.method == "POST":
        form = DiscussionPostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            messages.success(request, 'Post Updated!')
            return HttpResponseRedirect(reverse('profile'))
    else:
        form = DiscussionPostForm(instance=post)
        return render(request, 'discussionpost_edit.html', {'form': form})
        


@login_required
def post_delete(request, post_id):
    post = get_object_or_404(DiscussionPost, pk=post_id, author=request.user)
    if request.method == "POST":
        post.delete()
        messages.success(request, 'Post deleted!')
        return HttpResponseRedirect(reverse('profile'))
    else:
        messages.error(request, 'You can only delete your own post!')
        return HttpResponseRedirect(reverse('profile'))