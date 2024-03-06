from django.shortcuts import get_object_or_404, HttpResponseRedirect
from django.shortcuts import render, reverse
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Profile
from blog.models import Category, Post, Comment
from discussion.models import DiscussionPost, DiscussionComment
from discussion.forms import DiscussionPostForm


@login_required
def profile_page(request):
    user_profile = Profile.objects.get(user=request.user)
    categories = Category.objects.all()
    discussions = DiscussionPost.objects.filter(author=request.user)
    comments = Comment.objects.filter(author=request.user)
    discussion_comments = DiscussionComment.objects.filter(author=request.user)
    
    context = {
        "categories": categories,
        "profile": user_profile,
        "comments": comments,
        "discussion_comments": discussion_comments,
        "discussions": discussions,
    }

    return render(request, 'profilepage/profile.html', context)


@login_required
def discussion_edit(request, post_id):
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
def discussion_delete(request, pk):
    """
    View to delete discussion post
    """
    discussion_post = get_object_or_404(DiscussionPost, pk=pk)

    if discussion_post.author == request.user:
        discussion_post.delete()
        messages.success(request, 'Discussion deleted!')
    else:
        messages.error(request, 'You can only delete your own discussion!')

    return HttpResponseRedirect(reverse('profilepage/profile.html'))


@login_required
def comment_delete(request, slug, comment_id):
    post = get_object_or_404(queryset, slug=slug)
    comment = get_object_or_404(Comment, id=comment_id)
    if comment.author == request.user:
        comment.delete()
        messages.success(request, 'Comment deleted!')
    else:
        messages.error(request, 'You can only delete your own comments!')

    return HttpResponseRedirect(reverse('profile.html'))
