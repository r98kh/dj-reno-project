from django.shortcuts import render
from .models import Product
from django.views.generic import DetailView, ListView


# Create your views here.

class ProductsListView(ListView):
    template_name = 'product_module/products.html'
    model = Product
class ProductDetailView(DetailView):
    template_name = 'product_module/product_details.html'
    model = Product

