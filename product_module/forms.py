from django import forms

class ProductPerPageForm(forms.Form):
    choices = [(None, 'تعداد محصولات در هر صفحه'),(10, '10'), (50, '50'), (100, '100')] 
    items_per_page = forms.ChoiceField(choices=choices, widget=forms.Select(attrs={'onchange': 'this.form.submit();'}))

class SortingForm(forms.Form):
    CHOICES = [
        (None, 'مرتب سازی بر اساس'),
        ('price_asc', 'قیمت: کم به زیاد'),
        ('price_desc', 'قیمت: زیاد به کم'),
        ('date_desc', 'تاریخ: جدیدترین'),
        ('date_asc', 'تاریخ: قدیمی‌ترین'),
    ]

    sorting_option = forms.ChoiceField(
        choices=CHOICES,
        widget=forms.Select(attrs={'onchange': 'this.form.submit();'}),
    )
