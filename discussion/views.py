from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import DiscussionPost
from .forms import DiscussionPostForm
from blog.models import Post 

# Create your views here.

def discussion_list(request):
    posts = Post.objects.all() 
    return render(request, 'discussion/discussion_list.html', {'posts': posts})


def discussion_detail(request, pk):
    post = DiscussionPost.objects.get(pk=pk)
    return render(request, 'discussion/discussion_detail.html', {'post': post})


def discussion_create(request):
    if request.method == 'POST':
        form = DiscussionPostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('discussion_list')
    else:
        form = DiscussionPostForm()
    return render(request, 'discussion/discussion_form.html', {'form': form})