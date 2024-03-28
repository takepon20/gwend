from django.shortcuts import render
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic import FormView, CreateView # 追加
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from .forms import CustomUserCreationForm, CustomAuthenticationForm

class Login(LoginView):
    form_class = CustomAuthenticationForm
    template_name = 'account/login.html'
    success_url = reverse_lazy('job:list_job')

class Logout(LogoutView):
    success_url = reverse_lazy('index:index')

class Register(CreateView):
    form_class = CustomUserCreationForm
    template_name = 'account/register.html'
    success_url = reverse_lazy('account:login')
