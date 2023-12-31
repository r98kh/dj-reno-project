from django import forms
from .models import Comments

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comments
        fields = ['message']
        widgets = {
            'message': forms.Textarea(attrs={'class': 'form-control','placeholder':"پیام خود را وارد کنید" }),
        }
        labels = {
            'message': 'پیام',
        }