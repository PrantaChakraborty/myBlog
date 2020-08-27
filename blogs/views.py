from django.shortcuts import render
from .models import Post
# Create your views here.


def homeView(request):
    post_display = Post.objects.all()

    return render(request, 'blog/home.html', {'Post': post_display})
