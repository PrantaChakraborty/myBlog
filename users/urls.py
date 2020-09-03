from django.urls import path
from .views import SignUpPageView
from django.contrib.auth import views as auth_view


urlpatterns = [
    path('password_change/', auth_view.PasswordChangeView.as_view(template_name='account/password_change_form.html'),
         name='password_change'),
    path('password_change/done/',
         auth_view.PasswordChangeDoneView.as_view(template_name='account/password_change_done.html'),
         name='password_change_done'),
    path('password_reset/', auth_view.PasswordResetView.as_view(template_name='account/password_reset_form.html'),
         name='password_reset'),
    path('password_reset/done/',
         auth_view.PasswordResetDoneView.as_view(template_name='account/password_reset_done.html'),
         name='password_reset_done'),
    path('reset/<uidb64>/<token>/',
         auth_view.PasswordResetConfirmView.as_view(template_name='account/password_reset_confirm.html'),
         name='password_reset_confirm'),
    path('reset/done/',
         auth_view.PasswordResetCompleteView.as_view(template_name='account/password_reset_complete.html'),
         name='password_reset_complete'),
    path('signup/', SignUpPageView.as_view(), name='signup'),
]
