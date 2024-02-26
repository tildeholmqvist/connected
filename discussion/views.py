from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.views import generic
from django.contrib import messages
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from .models import DiscussionPost, Category, DiscussionComment
from .forms import DiscussionPostForm, DiscussionCommentForm
from blog.models import Post


class DiscussionIndex(generic.ListView):
    queryset = DiscussionPost.objects.all().order_by("-created_at")
    context_object_name = "discussions"
    paginate_by = 6
    template_name = "discussion/discussion_list.html"



def discussion_list(request):
    discussions = DiscussionPost.objects.all()
    return render(request, 'discussion/discussion_list.html', {'discussions': discussions})


def discussion_category(request, category):
    discussions = DiscussionPost.objects.filter(
        category__name=category).order_by("-created_at")
    context = {
        "category": category,
        "discussions": discussions,
    }
    return render(request, "discussion/discussion_category.html", context)


# This is the same view as in the blog_detail

def discussion_detail(request, pk):
    discussion = DiscussionPost.objects.get(pk=pk)
    form = DiscussionCommentForm()
    if request.method == "POST":
        form = DiscussionCommentForm(request.POST)
        if form.is_valid():
            comment = DiscussionComment(
                author=request.user,
                body=form.cleaned_data["body"],
                post=discussion,
            )
            comment.save()
            messages.add_message(
                request, messages.SUCCESS,
                'Comment submitted and awaiting approval'
                )
            return HttpResponseRedirect(request.path_info)

    comments = discussion.comments.all().order_by("-created_at")
    comment_count = discussion.comments.filter(approved=True).count()
    context = {
        "discussion": discussion,
        "comments": comments,
        "form": form,
    }
    return render(request, 'discussion/discussion_detail.html', context)


@login_required
def create_discussion(request):
    if request.method == 'POST':
        form = DiscussionPostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            messages.add_message(
                request, messages.SUCCESS,
                'Post submitted and awaiting approval'
                )
            return HttpResponseRedirect(request.path_info)
    else:
        form = DiscussionPostForm()

    form.fields['category'].queryset = Category.objects.all()
    return render(request, 'discussion/create_discussion.html', {'form': form})


def comment_delete(request, pk, comment_id):
    """
    View to delete comment
    """
    post = get_object_or_404(Post, pk=pk)
    discussion_comment = get_object_or_404(DiscussionComment, id=comment_id)
    if discussion_comment.author == request.user:
            discussion_comment.delete()
            messages.success(request, 'Comment deleted!')
    else:
        messages.error(request, 'You can only delete your own comments!')

    return HttpResponseRedirect(reverse('discussion_detail', kwargs={'pk': pk}))


#@login_required
#def profile(request):
#    user_profile = get_object_or_404(User, username=request.user.username)
#        context = {
#                    'user_profile': user_profile
#                            }
#
#                               return render(request, 'profile.html', context )