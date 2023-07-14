from django.views.generic import TemplateView


class AboutUsPageView(TemplateView):
    template_name = 'aboutus_module/aboutus.html'
