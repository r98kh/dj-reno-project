from django.db import models
from user_module.models import CustomUser
from product_module.models import Product
from blogs_module.models import Blogs
# Create your models here.

class Comments(models.Model):
    user = models.ForeignKey(CustomUser,models.CASCADE)
    message = models.TextField()
    created_date = models.DateField(auto_now_add=True)
    product = models.ForeignKey(Product,models.CASCADE,null= True,blank=True)
    blog = models.ForeignKey(Blogs,models.CASCADE,null= True,blank=True)
    