from django.db import models
from django.urls import reverse
from slugify import slugify


# Create your models here.

class ProductCategory(models.Model):
    title = models.CharField(
        max_length=300, db_index=True, verbose_name='عنوان')
    is_active = models.BooleanField(verbose_name='فعال / غیرفعال')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'دسته بندی'
        verbose_name_plural = 'دسته بندی ها'


class ProductBrand(models.Model):
    title = models.CharField(max_length=50, db_index=True)
    is_active = models.BooleanField(default=True)

    def __str__(self) -> str:
        return self.title


class productGallery(models.Model):
    image = models.ImageField(
        upload_to='images/product-gallery', verbose_name='تصویر')

    def __str__(self):
        return self.image.name

    class Meta:
        verbose_name = 'تصویر گالری'
        verbose_name_plural = 'گالری تصاویر'


class Attribute(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self) -> str:
        return self.name


class value(models.Model):
    value = models.CharField(max_length=50)

    def __str__(self) -> str:
        return self.value


class ProductAttribute(models.Model):
    attribute = models.ForeignKey(Attribute, models.CASCADE)
    values = models.ManyToManyField(value)

    def __str__(self) -> str:
        return self.attribute.name


class Product(models.Model):
    title = models.CharField(max_length=300, verbose_name='نام محصول')
    category = models.ManyToManyField(
        ProductCategory, related_name='product_categories', verbose_name='دسته بندی ها')
    brand = models.ForeignKey(ProductBrand, models.CASCADE, null=True)
    image = models.ImageField(
        upload_to='images/products', null=True, blank=True, verbose_name='تصویر محصول')
    gallery = models.ManyToManyField(productGallery)
    attribute = models.ManyToManyField(ProductAttribute)
    price = models.IntegerField(verbose_name='قیمت')
    description = models.TextField(verbose_name='توضیحات اصلی', db_index=True)
    slug = models.SlugField(default="", null=False, db_index=True, blank=True, max_length=200, unique=True,
                            verbose_name='عنوان در url')
    special = models.BooleanField(default=False)
    created_date = models.DateField(auto_now_add=True)
    quantity_sold = models.PositiveIntegerField(default=0)
    is_active = models.BooleanField(
        default=False, verbose_name='فعال / غیرفعال')
    is_delete = models.BooleanField(verbose_name='حذف شده / نشده')


    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.title} ({self.price})"

    class Meta:
        verbose_name = 'محصول'
        verbose_name_plural = 'محصولات'



