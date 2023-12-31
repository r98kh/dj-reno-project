from django.shortcuts import render
from django.views.generic import TemplateView
from . import models
from aboutus_module.models import AboutUs
from blogs_module.models import Blogs
from product_module.models import ProductCategory, Product
from cart_module.models import Order,OrderDetail
from contactus_module.forms import NewsLetterForm

# Create your views here.
def site_header_component(request):
    user_id = request.user.id
    try:
        user_order, created = Order.objects.get_or_create(user_id=user_id, is_paid=False)
        cart_detail = OrderDetail.objects.filter(order_id=user_order.id).all()
        total = 0
        for i in cart_detail:
            total += i.get_total_price()
        context = {
            'totalPrice': user_order.calculate_total_price(),
            'orders': cart_detail,
            'total': total,
            'logo': AboutUs.objects.first().logo

        }
    except:
        context = {
            'totalPrice':0,
            'orders': [],
            'total':0,
            'logo': AboutUs.objects.first().logo
        }    
    return render(request, 'shared/site_header_component.html',context)


def site_footer_component(request):
    form = NewsLetterForm()
    context = {
        'aboutus': AboutUs.objects.first(),
        'form': form
    }
    return render(request, 'shared/site_footer_component.html',context)


class homePageView(TemplateView):
    template_name = 'home_module/home.html'

    def get_context_data(self, **kwargs):
        context = super(homePageView, self).get_context_data(**kwargs)
        context['product_banner'] = models.HeaderProductBanner.objects.all()
        context['category_banner'] = models.HeaderCategoryBanner.objects.all()[:2]
        context['products'] = Product.objects.all().order_by('-created_date')
        context['specialProduct'] = Product.objects.filter(special=True)
        context['bestSeller'] = Product.objects.all().order_by('quantity_sold')[:5]
        context['category'] = ProductCategory.objects.all()
        context['blogs'] = Blogs.objects.all()
        return context
    
    def post(self, request, *args, **kwargs):
        form = NewsLetterForm(request.POST)
        if form.is_valid():
            form.save()
        return self.get(request, *args, **kwargs)