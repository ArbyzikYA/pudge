from .models import *
from django.contrib.auth.models import User
from django import forms
from django.conf import settings
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render
from django.forms.widgets import *

class UserRegistrationForm(UserCreationForm):
    username = forms.CharField(max_length=60)
    email = forms.EmailField(max_length=20)
    class Meta:
        model = MyUser
        fields = ('username', 'email',)
