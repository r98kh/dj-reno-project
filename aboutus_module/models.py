from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.

class SocialMedia(models.Model):
    name = models.CharField(max_length=20)
    url = models.URLField()

class AboutUs(models.Model):
    logo = models.ImageField(upload_to='images/logo')
    description = models.TextField()
    title = models.CharField(max_length=50)
    aboutus = models.TextField()
    address = models.TextField()
    phone = PhoneNumberField()
    email = models.EmailField()
    social_media = models.ManyToManyField(SocialMedia, null=True, blank=True)
    def __str__(self) -> str:
        return self.title