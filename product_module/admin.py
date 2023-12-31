from django.contrib import admin
from . import models
# Register your models here.


class ProductAdmin(admin.ModelAdmin):
    list_filter =  ['is_active']
    list_display = ['title', 'price', 'is_active', 'is_delete']
    list_editable = ['price', 'is_active']


admin.site.register(models.Product, ProductAdmin)
admin.site.register(models.Attribute)
admin.site.register(models.ProductAttribute)
admin.site.register(models.value)
admin.site.register(models.productGallery)
admin.site.register(models.ProductCategory)
admin.site.register(models.ProductBrand)