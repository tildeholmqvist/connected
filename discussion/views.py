from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.views import generic
from django.contrib import messages
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from .models import DiscussionPost, DiscussionComment
from .forms import DiscussionPostForm, DiscussionCommentForm
from blog.models import Post, Category


class DiscussionIndex(generic.ListView):
    queryset = DiscussionPost.objects.all().order_by("-created_at")
    context_object_name = "discussions"
    paginate_by = 6
    template_name = "discussion/discussion_list.html"


    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        return context


def discussion_list(request):
    discussions = Discussion.objects.all() 
    discussion.comment_count = discussion.comments.filter(approved=True).count()
    return render(request, 'discussion/discussion_list.html', {'discussions': discussions})

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
    discussion.comment_count = discussion.comments.filter(approved=True).count()

    categories = Category.objects.all() 
    context = {
        "discussion": discussion,
        "comments": comments,
        "form": form,
        "categories": categories,
        "discussion.comment_count": discussion.comment_count
    }
    return render(request, 'discussion/discussion_detail.html', context)


@login_required
def create_discussion(request):
    categories = Category.objects.all() 

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
            return redirect('discussion_list')
    else:
        form = DiscussionPostForm()

    return render(request, 'discussion/create_discussion.html', {'form': form, 'categories': categories})


def comment_edit(request, pk, comment_id):
    categories = Category.objects.all() 
    """
    View to edit comments
    """
    if request.method == "POST":
        discussion_post = get_object_or_404(DiscussionPost, pk=pk)
        comment = get_object_or_404(DiscussionComment, id=comment_id)
        comment_form = DiscussionCommentForm(data=request.POST, instance=comment)

        if comment_form.is_valid() and comment.author == request.user:
            comment = comment_form.save(commit=False)
            comment.post = discussion_post
            comment.approved = False
            comment.save()
            messages.success(request, 'Comment Updated!')
        else:
            messages.error(request, 'Error updating comment!')
        return HttpResponseRedirect(reverse('discussion_detail', kwargs={'pk': pk}))
    else:
        post = get_object_or_404(DiscussionPost, pk=pk)
        comment = get_object_or_404(DiscussionComment, id=comment_id)
        comment_form = DiscussionCommentForm(instance=comment)
        context = {
            "form": comment_form,
            "categories": categories
        }

    return render(request, "discussion/edit_discussion_comment.html", context)


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