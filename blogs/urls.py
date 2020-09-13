from django.urls import path
from .views import (
    home_view,
    post_detail_view,
    AboutView,
    PostCreateView,
    PostUpdateView,
    PostDeleteView,
    PostSearchListView,
#    PostCategoryView,
    post_category_view,

)

urlpatterns = [
    path('', home_view, name='home'),
    path('post/create/', PostCreateView.as_view(), name='create_blog'),
    path('post/about_view/', AboutView.as_view(), name='about'),
    path('post/<uuid:pk>/', post_detail_view, name='detail_view'),
    path('post/<uuid:pk>/edit/', PostUpdateView.as_view(), name='blog_edit'),
    path('post/<uuid:pk>/delete/', PostDeleteView.as_view(), name='blot_delete'),
    path('post/search/', PostSearchListView.as_view(), name='search_result'),
    path('post/category/<int:pk>/', post_category_view, name='post_category_view'),

]
