from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Profile

# Create your views here.

@login_required
def profile_page(request):
    user = request.user
    return render(request, 'profilepage/profile.html', {'user': user})