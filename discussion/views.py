from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from .models import DiscussionPost, Category, DiscussionComment
from .forms import DiscussionPostForm, DiscussionCommentForm
from blog.models import Post


def discussion_list(request):
    discussions = DiscussionPost.objects.all()
    paginate_by = 6
    return render(request, 'discussion/discussion_list.html', {'discussions': discussions})


def discussion_category(request, category):
    discussions = DiscussionPost.objects.filter(
        categories__name=category).order_by("-created_at")
    context = {
        "category": category,
        "discussions": discussions,
    }
    return render(request, "discussion/discussion_list.html", context)


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
            return redirect('discussion_list')
    else:
        form = DiscussionPostForm()

    form.fields['category'].queryset = Category.objects.all()
    return render(request, 'discussion/create_discussion.html', {'form': form})