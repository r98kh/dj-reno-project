from django.shortcuts import render
from django.views.generic import TemplateView
from . import models
# Create your views here.

class AboutUsView(TemplateView):
    template_name = 'aboutus_module/aboutus.html'
    model = models.AboutUs

    def get_context_data(self, **kwargs):
        context = super(AboutUsView, self).get_context_data(**kwargs)
        context['information'] = models.AboutUs.objects.first()

        return context