from django.db import models
from django.contrib.auth.models import AbstractUser
from phonenumber_field.modelfields import PhoneNumberField


# Create your models here.

class CustomUser(AbstractUser):
    phone_number = PhoneNumberField(null=True, blank=True, unique=True)

