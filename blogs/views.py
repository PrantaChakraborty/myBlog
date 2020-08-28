from django.core.paginator import Paginator
from django.shortcuts import render
from .models import Post
from django.views.generic import DetailView
# Create your views here.


# list view
def homeView(request):
    post_display = Post.objects.all()
    paginator = Paginator(post_display, 3)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'blog/home.html', {'page_obj': page_obj})


# detail view for blog
class PostDetailView(DetailView):
    model = Post
    template_name = 'blog/blog_detail.html'
    context_object_name = 'post'
