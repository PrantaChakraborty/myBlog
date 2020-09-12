from django.urls import path, re_path
from .views import (
    SignUpPageView,
    ProfilePageView,
    CustomPasswordChangeView,
    CustomPasswordResetFormKeyView,
    CustomPasswordResetFormKeyDoneView
)

urlpatterns = [
    path(r"^password/reset/key/(?P<uidb36>[0-9A-Za-z]+)-(?P<key>.+)/$",
         CustomPasswordResetFormKeyView.as_view(), name="account_reset_password_from_key"),

    path('password/reset/key/done/', CustomPasswordResetFormKeyDoneView.as_view(),
         name='account_reset_password_from_key_done'),

    path("password/change/", CustomPasswordChangeView.as_view(), name="account_password_change"),

    path('profile/', ProfilePageView.as_view(), name='profile_view'),

    path('signup/', SignUpPageView.as_view(), name='signup'),
]
