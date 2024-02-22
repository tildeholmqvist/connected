from django.shortcuts import render, get_object_or_404
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.views import generic
from .models import Post, Comment
from .forms import CommentForm, PostForm


# Create your views here.

class BlogList(generic.ListView):
    queryset = Post.objects.all().order_by("-created_at")
    template_name = "blog/index.html"
    context_object_name = "posts"
    paginate_by =  6


def blog_category(request, category):
    posts = Post.objects.filter(
        category__name__contains=category).order_by("-created_at")
    context = {
        "category": category,
        "posts": posts,
    }
    return render(request, "blog/category.html", context)


def blog_detail(request, pk):
    queryset = Post.objects.all()
    post = get_object_or_404(queryset, pk=pk)
    form = CommentForm()
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = Comment(
                author=request.user,
                body=form.cleaned_data["body"],
                post=post,
            )
            comment.save()
            # From walkthrough
            messages.add_message(
                request, messages.SUCCESS,
                'Comment submitted and awaiting approval'
                )
            return HttpResponseRedirect(request.path_info)

    comments = post.comments.all().order_by("-created_at")
    comment_count = post.comments.filter(approved=True).count()
    context = {
        "post": post,
        "comments": comments,
        "comment_count": comment_count,
        "form": CommentForm(),
    }

    return render(request, "blog/blog_detail.html", context)

# WALKTHROUGH

def comment_edit(request, comment_id):
    """
    view to edit comments
    """
    if request.method == "POST":

        queryset = Post.objects.filter(status=1)
        post = get_object_or_404(queryset)
        comment = get_object_or_404(Comment, pk=comment_id)
        comment_form = CommentForm(data=request.POST, instance=comment)

        if comment_form.is_valid() and comment.author == request.user:
            comment = comment_form.save(commit=False)
            comment.post = post
            comment.approved = False
            comment.save()
            messages.add_message(request, messages.SUCCESS, 'Comment Updated!')
        else:
            messages.add_message(
                request, messages.ERROR,
                'Error updating comment!')

    return HttpResponseRedirect(reverse('blog_detail'))

def about(request):
    return render(request, 'about.html')


# FROM WALKTHROUGH

def comment_edit(request, pk, comment_id):
    """
    View to edit comments
    """
    if request.method == "POST":
        post = get_object_or_404(Post, pk=pk)
        comment = get_object_or_404(Comment, pk=comment_id)
        comment_form = CommentForm(data=request.POST, instance=comment)

        if comment_form.is_valid() and comment.author == request.user:
            comment = comment_form.save(commit=False)
            comment.post = post
            comment.approved = False
            comment.save()
            messages.success(request, 'Comment Updated!')
        else:
            messages.error(request, 'Error updating comment!')

    return HttpResponseRedirect(reverse('blog_detail', kwargs={'pk': pk}))

def comment_delete(request, pk, comment_id):
    """
    View to delete comment
    """
    post = get_object_or_404(Post, pk=pk)
    comment = get_object_or_404(Comment, pk=comment_id)

    if comment.author == request.user:
        comment.delete()
        messages.success(request, 'Comment deleted!')
    else:
        messages.error(request, 'You can only delete your own comments!')

    return HttpResponseRedirect(reverse('blog_detail', kwargs={'pk': pk}))