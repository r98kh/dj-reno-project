from django import forms
from django.core import validators
from django.core.exceptions import ValidationError

from user_module.models import CustomUser


# class LoginForm(forms.ModelForm):
#     class Meta:
#         model = CustomUser
#         fields = ['email', 'password']

