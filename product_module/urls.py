from django.urls import path
from . import views

urlpatterns = [
    path('', views.ProductsListView.as_view(), name='products-list'),
    path('cat/<cat>', views.ProductsListView.as_view(), name='product-categories-list'),
    path('brand/<brand>', views.ProductsListView.as_view(), name='product-brand-list'),
    path('<slug:slug>', views.ProductDetailView.as_view(), name='product-detail'),

]
