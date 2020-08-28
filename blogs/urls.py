from django.urls import path
from .views import homeView, PostDetailView

urlpatterns = [
    path('', homeView, name='home'),
    path('post/<uuid:pk>/', PostDetailView.as_view(), name='detail_view')

]