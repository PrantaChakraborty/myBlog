from django.urls import reverse_lazy
from django.views import generic
from allauth.account.views import PasswordChangeView

from .forms import CustomUserCreationForm


class SignUpPageView(generic.CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('account_login')
    template_name = 'account/signup.html'


class PorfilePageView(generic.TemplateView):
    template_name = 'users/profile.html'


class CustomPasswordChangeView(PasswordChangeView):
    success_url = reverse_lazy('account_login')

