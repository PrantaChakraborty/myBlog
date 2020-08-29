from django.urls import path
from .views import homeView, PostDetailView, AboutView, BlogCreateView, createblog

urlpatterns = [
    path('post/create/', BlogCreateView.as_view(), name='create_blog'),
    path('post/about_view/', AboutView.as_view(), name='about'),
    path('post/<uuid:pk>/', PostDetailView.as_view(), name='detail_view'),
    path('', homeView, name='home'),

]