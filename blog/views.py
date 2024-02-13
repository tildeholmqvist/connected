from django.shortcuts import render, get_object_or_404
from .models import Post, Comment

# Create your views here.

def blog_list(request):
    posts = Post.objects.all().order_by("-created_at")
    context = {
        "posts": posts,
    }

    return render(request, "blog/index.html", context)


def blog_category(request, category):
    posts = Post.objects.filter(
        categories__name__contains=category).order_by("-created_at")
    context = {
        "category": category,
        "posts": posts,
    }
    return render(request, "blog/category.html", context)


def blog_detail(request, pk):
    post = Post.objects.get(pk=pk)
    comments = Comment.objects.filter(post=post)
    context = {
        "post": post,
        "comments": comments,
    }

    return render(request, "blog/blog_detail.html", context)

