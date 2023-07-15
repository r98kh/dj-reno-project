from django.shortcuts import render
from django.views.generic import TemplateView

from blogs_module.models import Blogs
from product_module.models import ProductCategory, Product


# Create your views here.
def site_header_component(request):
    return render(request, 'shared/site_header_component.html', {})


def site_footer_component(request):
    return render(request, 'shared/site_footer_component.html', {})


class homePageView(TemplateView):
    template_name = 'home_module/home.html'

    def get_context_data(self, **kwargs):
        context = super(homePageView, self).get_context_data(**kwargs)
        context['products'] = Product.objects.all().order_by('-created_date')
        context['specialProduct'] = Product.objects.filter(special=True)
        context['category'] = ProductCategory.objects.all()
        context['blogs'] = Blogs.objects.all()
        return context
