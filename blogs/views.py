from django.core.paginator import Paginator
from django.db.models import Q
from django.shortcuts import render
from django.urls import reverse_lazy
from django.contrib.auth.mixins import (
    LoginRequiredMixin,
    UserPassesTestMixin)
from .models import Post, Category
from django.views.generic import DetailView, TemplateView, ListView
from django.views.generic.edit import UpdateView, DeleteView, CreateView
from .forms import PostCreateForm, PostUpdateForm


# Create your views here.


# list view
def homeView(request):
    post_display = Post.objects.all()
    category_display = Category.objects.all()
    paginator = Paginator(post_display, 3)  # display 3 post per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'page_obj': page_obj,
        'Categories': category_display
    }
    return render(request, 'blog/home.html', context=context)


# detail view for blog
class PostDetailView(LoginRequiredMixin, DetailView):
    model = Post
    template_name = 'blog/blog_detail.html'
    context_object_name = 'post'
    login_url = 'account_login'


class AboutView(LoginRequiredMixin, TemplateView):
    template_name = 'about.html'
    login_url = 'account_login'


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    template_name = 'blog/create_blog.html'
    form_class = PostCreateForm
    login_url = 'account_login'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    template_name = 'blog/edit_blog.html'
    form_class = PostUpdateForm
    login_url = 'account_login'

    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    template_name = 'blog/delete_blog.html'
    success_url = reverse_lazy('home')
    login_url = 'account_login'

    def test_func(self):  # new
        obj = self.get_object()
        return obj.author == self.request.user


class PostSearchListView(LoginRequiredMixin, ListView):
    model = Post
    context_object_name = 'posts'
    template_name = 'blog/search_result.html'
    login_url = 'account_login'

    def get_queryset(self):
        query = self.request.GET.get('q')
        return Post.objects.filter(Q(title__icontains=query))
