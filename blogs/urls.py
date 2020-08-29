from django.urls import path
from .views import homeView, PostDetailView, AboutView, BlogCreateView

urlpatterns = [
    path('', homeView, name='home'),
    path('post/create/', BlogCreateView.as_view(), name='create_blog'),
    path('post/about_view/', AboutView.as_view(template_name= 'about.html'), name='about'),
    path('post/<uuid:pk>/', PostDetailView.as_view(), name='detail_view'),

]
