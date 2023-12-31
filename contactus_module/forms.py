from django import forms
from . import models


class ContactForm(forms.ModelForm):
    class Meta:
        model = models.ContactUs
        fields = ['name', 'email', 'message']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control','placeholder':"نام خود را وارد کنید" }),
            'email': forms.EmailInput(attrs={'class': 'form-control','placeholder':"ایمیل خود را وارد کنید" }),
            'message': forms.Textarea(attrs={'class': 'form-control','placeholder':"پیام خود را وارد کنید" }),
        }
        labels = {
            'name': 'نام',
            'email': 'ایمیل',
            'message': 'پیام',
        }

class NewsLetterForm(forms.ModelForm):
    class Meta:
        model = models.NewsLetter
        fields = ['email']
        widgets = {
            'email': forms.EmailInput(attrs={'class': 'form-control','placeholder':"ایمیل خود را وارد کنید" }),
        }
