from django.contrib.auth.views import LoginView
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView

from users.forms import LoginForm, RegisterForm


# Create your views here.
class Login(LoginView):
    form_class = LoginForm
    template_name = 'users/login.html'
    extra_context = {
        'title': 'Логин'
    }

    def get_success_url(self):
        return reverse_lazy('main_page')


class Register(CreateView):
    form_class = RegisterForm
    template_name = 'users/register.html'
    success_url = reverse_lazy('main_page')

    extra_context = {
        'title': 'Регистрация'
    }