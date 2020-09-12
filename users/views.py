from django.urls import reverse_lazy
from django.views import generic
from allauth.account.views import PasswordChangeView, PasswordResetFromKeyView, PasswordResetFromKeyDoneView

from .forms import CustomUserCreationForm


class SignUpPageView(generic.CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('account_login')
    template_name = 'account/signup.html'


class ProfilePageView(generic.TemplateView):
    template_name = 'users/profile.html'


class CustomPasswordChangeView(PasswordChangeView):
    template_name = 'account/password_change.html'
    success_url = reverse_lazy('account_login')


class CustomPasswordResetFormKeyView(PasswordResetFromKeyView):
    template_name = 'account/password_reset_form_key.html'
    success_url = reverse_lazy('account_reset_password_from_key_done')


class CustomPasswordResetFormKeyDoneView(PasswordResetFromKeyDoneView):
    template_name = 'account/password_reset_form_key_done.html'
