from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import DiscussionPost
from .forms import DiscussionPostForm
from blog.models import Post
from .models import Category

def discussion_list(request):
    discussions = DiscussionPost.objects.all()
    return render(request, 'discussion/discussion_list.html', {'discussions': discussions})

def discussion_detail(request, pk):
    discussion = DiscussionPost.objects.get(pk=pk)
    return render(request, 'discussion/discussion_detail.html', {'discussion': discussion})

def discussion_category(request, category):
    discussions = DiscussionPost.objects.filter(category__name__contains=category).order_by("-created_at")
    context = {
        "category": category,
        "discussions": discussions,
    }
    return render(request, "discussion/discussion_list.html", context)

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