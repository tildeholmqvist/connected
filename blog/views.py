from django.shortcuts import render, get_object_or_404
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.views import generic
from django.urls import reverse
from .models import Post, Comment, Category
from .forms import CommentForm, PostForm


# Create your views here.

class BlogList(generic.ListView):
    queryset = Post.objects.all().order_by("-created_at")
    template_name = "blog/index.html"
    context_object_name = "posts"
    paginate_by = 6

    def get_context_data(self, **kwargs):
        context = super(BlogList, self).get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        return context


def blog_category(request, category):
    posts = Post.objects.filter(
        category__name__contains=category).order_by("-created_at")
    categories = Category.objects.all()
    context = {
        "category": category,
        "posts": posts,
        "categories": categories,
    }
    return render(request, "blog/category.html", context)


def blog_detail(request, slug):
    queryset = Post.objects.all()
    post = get_object_or_404(queryset, slug=slug)
    form = CommentForm(request.POST)
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
    else:
        form = CommentForm()

    comments = post.comments.all().order_by("-created_at")
    comment_count = post.comments.filter(approved=True).count()

    categories = Category.objects.all()
    context = {
        "post": post,
        "comments": comments,
        "categories": categories,
        "comment_count": comment_count,
        "form": form,
    }

    categories = Category.objects.all()
    return render(request, "blog/blog_detail.html", context)


def about(request):
    categories = Category.objects.all()
    return render(request, 'blog/about.html', {'categories': categories})

# From Code Institutes Walk Through Project, "I think therefor I blog",
# function to edit and delete comments


def comment_edit(request, slug, comment_id):
    categories = Category.objects.all()
    """
    View to edit comments
    """
    if request.method == "POST":
        post = get_object_or_404(Post, slug=slug)
        comment = get_object_or_404(Comment, id=comment_id)
        comment_form = CommentForm(data=request.POST, instance=comment)

        if comment_form.is_valid() and comment.author == request.user:
            comment = comment_form.save(commit=False)
            comment.post = post
            comment.approved = False
            comment.save()
            messages.success(request, 'Comment Updated!')
        else:
            messages.error(request, 'Error updating comment!')
        return HttpResponseRedirect(
            reverse('blog_detail', kwargs={'slug': slug}))
    else:
        post = get_object_or_404(Post, slug=slug)
        comment = get_object_or_404(Comment, id=comment_id)
        comment_form = CommentForm(instance=comment)
        context = {
            "form": comment_form,
            "categories": categories
        }

    return render(request, "blog/edit_comment.html", context)


def comment_delete(request, slug, comment_id):
    """
    View to delete comment
    """
    post = get_object_or_404(Post, slug=slug)
    comment = get_object_or_404(Comment, id=comment_id)

    if comment.author == request.user:
        comment.delete()
        messages.success(request, 'Comment deleted!')
    else:
        messages.error(request, 'You can only delete your own comments!')

    return HttpResponseRedirect(reverse('blog_detail', kwargs={'slug': slug}))
