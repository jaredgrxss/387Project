from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic
from . import forms
# Create your views here.

class SignUp(generic.CreateView):
    template_name = 'accounts/signup.html'
    form_class = forms.UserCreateForm
    success_url = reverse_lazy('accounts:login')
