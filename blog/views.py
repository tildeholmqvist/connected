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
        categories__name__contains=category).order_by("-created_at")
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
            return HttpResponseRedirect(request.path_info)

    comments = Comment.objects.filter(post=post)
    context = {
        "post": post,
        "comments": comments,
        "form": CommentForm(),
    }
    return render(request, "blog/blog_detail.html", context)

def about(request):
    return render(request, 'about.html')