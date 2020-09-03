from django.urls import path, re_path
from .views import SignUpPageView, PorfilePageView, CustomPasswordChangeView
from . import views


urlpatterns = [
    path(r"^password/change/$", CustomPasswordChangeView.as_view(), name="account_password_change"),
    path('profile/', PorfilePageView.as_view(), name='profile_view'),
    path('signup/', SignUpPageView.as_view(), name='signup'),
]
