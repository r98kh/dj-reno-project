from typing import Any
from django.shortcuts import render
from django.views.generic.edit import FormView
from . import models,forms
from aboutus_module.models import AboutUs
# Create your views here.

class ContactUsView(FormView):
    template_name = 'contactus_module/contactus.html'
    form_class = forms.ContactForm
    success_url = '/contact-us/'

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)
    # model = models.ContactUs

    def get_context_data(self, *args, **kwargs):
        context = super(ContactUsView, self).get_context_data(
            *args, **kwargs)
        
        context['aboutus'] = AboutUs.objects.first()
        return context