from django.urls import path
from .views import (
        homeView,
        post_detail_view,
        AboutView,
        PostCreateView,
        PostUpdateView,
        PostDeleteView,
        PostSearchListView,
        PostCategoryView,

)

urlpatterns = [
    path('', homeView, name='home'),
    path('post/create/', PostCreateView.as_view(), name='create_blog'),
    path('post/about_view/', AboutView.as_view(), name='about'),
    path('post/<uuid:pk>/', post_detail_view, name='detail_view'),
    path('post/<uuid:pk>/edit/', PostUpdateView.as_view(), name='blog_edit'),
    path('post/<uuid:pk>/delete/', PostDeleteView.as_view(), name='blot_delete'),
    path('post/search/', PostSearchListView.as_view(), name='search_result'),
    path('post/category/<int:pk>/', PostCategoryView.as_view(), name='post_category_view'),

]
