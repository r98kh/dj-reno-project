from . import models
from django.views.generic import DetailView, ListView
from django.shortcuts import render
from .models import Product
from django.db.models import Q
from comment_module.forms import CommentForm
from comment_module.models import Comments
from user_module.models import FavoriteProduct
from . import forms

# Create your views here.


class ProductsListView(ListView):
    template_name = 'product_module/products.html'
    model = models.Product

    def get_queryset(self):
        query = super(ProductsListView, self).get_queryset()
        selectedCategory = self.kwargs.get('cat')
        selectedBrand = self.kwargs.get('brand')
        search = self.request.GET.get('q')
        min_price = self.request.GET.get('min_price')
        max_price = self.request.GET.get('max_price')
        sorting_option = self.request.GET.get('sorting_option')

        if sorting_option == 'price_asc':
            query = query.order_by('price')
        elif sorting_option == 'price_desc':
            query = query.order_by('-price')
        elif sorting_option == 'date_desc':
            query = query.order_by('-created_date')
        elif sorting_option == 'date_asc':
            query = query.order_by('created_date')

        if min_price or max_price:
            query = query.filter(price__gte=min_price, price__lte=max_price)
        if search:
            query = query.filter(Q(title__icontains=search)
                                 | Q(description__icontains=search))
        if selectedBrand:
            query = query.filter(brand__title__iexact=selectedBrand)
        if selectedCategory is not None:
            query = query.filter(category__title__iexact=selectedCategory)
        return query

    def get_context_data(self, *args, **kwargs):
        context = super(ProductsListView, self).get_context_data(
            *args, **kwargs)
        products = models.Product.objects.all()
        context['product_count'] = products.count()
        context['max_price'] = products.order_by('-price').first().price
        context['new_product'] = products.order_by('created_date')[:5]
        context['category'] = models.ProductCategory.objects.all()
        context['brands'] = models.ProductBrand.objects.filter(
            is_active=True)
        context['ProductPerPageForm'] = forms.ProductPerPageForm(
            self.request.GET)
        context['SortingForm'] = forms.SortingForm(self.request.GET)
        return context

    def get_paginate_by(self, queryset):
        form = forms.ProductPerPageForm(self.request.GET)
        if form.is_valid():
            items_per_page = form.cleaned_data['items_per_page']
            return items_per_page or self.paginate_by

        return self.paginate_by

class ProductDetailView(DetailView):
    template_name = 'product_module/product_details.html'
    model = models.Product

    def get_context_data(self, *args, **kwargs):
        context = super(ProductDetailView, self).get_context_data(
            *args, **kwargs)
        brands = models.ProductBrand.objects.all()
        new_product = models.Product.objects.order_by('created_date')[:5]
        comments = Comments.objects.filter(product=self.object)
        context['comments'] = comments
        context['comment_form'] = CommentForm()

        context['brands'] = brands
        context['new_product'] = new_product
        context['share_url'] = 'https://example.com/my-page'
        return context

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            product = self.get_object()
            favoriteList, create = FavoriteProduct.objects.get_or_create(
                user=self.request.user, product=product)
            favoriteList.save()
        return super().get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.user = self.request.user
            comment.product = self.get_object()
            comment.save()
        return self.get(request, *args, **kwargs)
