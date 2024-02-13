from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from .models import Post, Comment
from blog.forms import CommentForm

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
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = Comment(
                author=request.user, 
                body=form.cleaned_data["body"],
                post=post,
            )
            comment.save()
            return HttpResponseRedirect(request.path_info)
    else:
        form = CommentForm() 

    comments = Comment.objects.filter(post=post)
    context = {
        "post": post,
        "comments": comments,
        "form": form,
    }

    return render(request, "blog/blog_detail.html", context)
