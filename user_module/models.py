from django.db import models
from django.contrib.auth.models import AbstractUser
from phonenumber_field.modelfields import PhoneNumberField
from product_module.models import Product


# Create your models here.
countries =( 
    ("1", "ایران"), 

) 



class CustomUser(AbstractUser):
    phone_number = PhoneNumberField(null=True, blank=True, unique=True)

class BillingDetails(models.Model):
    Country = models.CharField(max_length=50, choices=countries)
    state = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    address = models.TextField()
    postal_code = models.CharField(max_length=10)
    user = models.ForeignKey(CustomUser,on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.postal_code

class FavoriteProduct(models.Model):
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    user = models.ForeignKey(CustomUser,on_delete=models.CASCADE)