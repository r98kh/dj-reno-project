from django.db import models
from product_module.models import Product,ProductCategory
# Create your models here.

class HeaderProductBanner(models.Model):
    product = models.OneToOneField(Product,models.CASCADE)
    image = models.ImageField(upload_to='images/products')

class HeaderCategoryBanner(models.Model):
    category = models.OneToOneField(ProductCategory,models.CASCADE)
    image = models.ImageField(upload_to='images/products')