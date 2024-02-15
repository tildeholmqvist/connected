from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.views import generic
from .models import Post, Comment
from blog.forms import CommentForm
from .forms import PostForm

# Create your views here.

class BlogList(generic.ListView):
    queryset = Post.objects.all().order_by("-created_at")
    template_name = "blog/index.html"
    paginate_by = 6


    
def blog_category(request, category):
    posts = Post.objects.filter(
        categories__name__contains=category).order_by("-created_at")
    context = {
        "category": category,
        "posts": posts,
    }
    return render(request, "blog/category.html", context)


def blog_detail(request):
    queryset = Post.objects.filter(status=1)
    post = get_object_or_404(queryset)
    comments = post.comments.all().order_by("-created_on")
    comment_count = post.comments.filter(apporoved=True).count()
    if request.method == "POST":
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.author = request.user
            comment.post = post
            comment.save()
            messages.add_message(
                request, messages.SUCCESS,
                'Comment submitted and awaiting approval'
            )

    comment_form = CommentForm()

    return render(
        request,
        "blog/post_detail.html",
        {
            "post": post,
            "comments": comments,
            "comment_count": comment_count,
            "comment_form": comment_form,
        },
    )