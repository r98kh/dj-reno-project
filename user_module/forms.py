from django import forms
from django.core import validators
from django.core.exceptions import ValidationError
from django.contrib.auth.forms import UserChangeForm
from phonenumber_field.formfields import PhoneNumberField

from user_module.models import CustomUser,BillingDetails


class UserForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = [ 'first_name', 'last_name', 'email', 'phone_number' ]
        labels = {
            'first_name': 'نام',
            'last_name': 'نام خانوادگی',
            'email': 'ایمیل',
            'phone_number': 'شماره تماس',
        }
        widgets = {
            'phone_number': forms.TextInput(attrs={'value':'+98',}),
        }

class BillingDetailsForm(forms.ModelForm):
    class Meta:
        model = BillingDetails
        fields = ['Country','state', 'city', 'address', 'postal_code']
        widgets = {
            'city': forms.Select(),
            'state': forms.Select(attrs={'onchange': 'update_city()'}),
            'Country': forms.Select(attrs={'onchange': 'update_states()'}),
        }
        labels = {
            'Country': 'کشور',
            'state': 'استان',
            'city': 'شهر',
            'address': 'آدرس',
            'postal_code': 'کدپستی',
        }