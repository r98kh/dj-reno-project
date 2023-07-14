from django.db import models
from user_module.models import  CustomUser
from django.utils.text import slugify

class Blogs(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField(default="", null=False, db_index=True, blank=True, max_length=200, unique=True,
                            verbose_name='Slug')
    image = models.ImageField(upload_to='blog/', null=True, blank=True)
    description = models.TextField()
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    created_date = models.DateField(auto_created=True)
    demonstrable = models.BooleanField(default=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)


class Comments(models.Model):
    pass


