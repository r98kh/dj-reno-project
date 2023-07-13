from django.shortcuts import render
from django.views.generic import TemplateView


# Create your views here.
def site_header_component(request):
    return render(request, 'shared/site_header_component.html', {})


def site_footer_component(request):
    return render(request, 'shared/site_footer_component.html', {})

class homePageView(TemplateView):
    template_name = 'home_module/home.html'
