from django.urls import path
from .views import homeView, PostDetailView, AboutView

urlpatterns = [
    path('', homeView, name='home'),
    path('post/<uuid:pk>/', PostDetailView.as_view(), name='detail_view'),
    path('post/about_view/', AboutView.as_view(), name='about'),

]