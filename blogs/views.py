from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.db.models import Q
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.contrib.auth.mixins import (
    LoginRequiredMixin,
    UserPassesTestMixin
)
from .models import Post, Category, Comment
from django.views.generic import DetailView, TemplateView, ListView
from django.views.generic.edit import UpdateView, DeleteView, CreateView
from .forms import PostCreateForm, PostUpdateForm, CommentCreateForm, CommentUpdateForm


# Create your views here.


# list view
def home_view(request):
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

'''
# detail view for blog
class PostDetailView(LoginRequiredMixin, DetailView):
    model = Post
    template_name = 'blog/blog_detail.html'
    context_object_name = 'post'
    login_url = 'account_login'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['comments'] = Comment.objects.filter(post=self.object)
        context['form'] = CommentCreateForm()
        return context
'''


@login_required
def post_detail_view(request, pk):
    post = get_object_or_404(Post, id=pk)
    comments = post.comments.filter(active=True)
    template_name = 'blog/blog_detail.html'
    if request.method == 'POST':
        comment_form = CommentCreateForm(data=request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.author = request.user
            new_comment.post = post
            new_comment.save()
            comment_form = CommentCreateForm()  # clearing the comment filed after submit

    else:
        comment_form = CommentCreateForm()
    return render(request, template_name, {'post': post,
                                           'comments': comments,
                                           'comment_form': comment_form
                                           })


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

# class based post category view
'''
class PostCategoryView(LoginRequiredMixin, ListView):
    model = Post
    context_object_name = 'categories'
    template_name = 'blog/post_category_view.html'
    login_url = 'account_login'

    def get_queryset(self):
        return Post.objects.filter(category_id=self.kwargs.get('pk'))
'''
# function based post category view


@login_required()
def post_category_view(request, pk):
    post_categories = Post.objects.filter(category_id=pk)
    posts = Post.objects.all()
    paginator = Paginator(post_categories, 3)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    template = 'blog/post_category_view.html'
    context = {
        'page_obj': page_obj,
        'posts': posts
    }
    return render(request, template, context)
