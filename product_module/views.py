from .models import Product
from django.views.generic import DetailView, ListView
from .models import productFeatures, productGallery


# Create your views here.

class ProductsListView(ListView):
    template_name = 'product_module/products.html'
    model = Product

    def get_queryset(self):
        query = super(ProductsListView, self).get_queryset()
        category_name = self.kwargs.get('cat')

        if category_name is not None:
            query = query.filter(category__url_title__iexact=category_name)
        return query


class ProductDetailView(DetailView):
    template_name = 'product_module/product_details.html'
    model = Product

    def get_context_data(self, *args, **kwargs):
        context = super(ProductDetailView, self).get_context_data(*args, **kwargs)
        product = kwargs.get('object')
        context['gallery'] = productGallery.objects.filter(product_id=product.id).all()
        context['features'] = productFeatures.objects.filter(product_id=product.id).all()
        return context
