from django.urls import path
from .views import (
        homeView,
        PostDetailView,
        AboutView,
        PostCreateView,
        PostUpdateView,
        PostDeleteView,
)

urlpatterns = [
    path('', homeView, name='home'),
    path('post/create/', PostCreateView.as_view(), name='create_blog'),
    path('post/about_view/', AboutView.as_view(), name='about'),
    path('post/<uuid:pk>/', PostDetailView.as_view(), name='detail_view'),
    path('post/<uuid:pk>/edit/', PostUpdateView.as_view(), name='blog_edit'),
    path('post/<uuid:pk>/delete/', PostDeleteView.as_view(), name='blot_delete'),

]
