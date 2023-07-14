from django.views.generic import TemplateView


class ContactUsPageView(TemplateView):
    template_name = 'contactus_module/contactus.html'
