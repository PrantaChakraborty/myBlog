from django.core.paginator import Paginator
from django.shortcuts import render
from .models import Post, Category
from django.views.generic import DetailView, TemplateView
# Create your views here.


# list view
def homeView(request):
    post_display = Post.objects.all()
    category_display = Category.objects.all()
    paginator = Paginator(post_display, 3) # display 3 post per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
            'page_obj': page_obj,
            'Categories': category_display
            }
    return render(request, 'blog/home.html', context=context)


# detail view for blog
class PostDetailView(DetailView):
    model = Post
    template_name = 'blog/blog_detail.html'
    context_object_name = 'post'


class AboutView(TemplateView):
    template_name = 'about.html'
