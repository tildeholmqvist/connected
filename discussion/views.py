from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import DiscussionPost
from .forms import DiscussionPostForm
from blog.models import Post

def discussion_list(request):
    discussion = DiscussionPost.objects.all()
    return render(request, 'discussion/discussion_list.html', {'discussion': discussion})

def discussion_detail(request, pk):
    discussion = DiscussionPost.objects.get(pk=pk)
    return render(request, 'discussion/discussion_detail.html', {'discussion': discussion})

@login_required
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
    
    discussions = DiscussionPost.objects.all()
    return render(request, 'discussion/discussion_list.html', {'form': form, 'discussions': discussions})
