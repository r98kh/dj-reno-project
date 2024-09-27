# Generated by Django 4.2.3 on 2023-12-31 10:25

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("product_module", "0012_remove_productattribute_product_product_attribute"),
        ("user_module", "0008_alter_billingdetails_user"),
    ]

    operations = [
        migrations.CreateModel(
            name="FavoriteProduct",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("product", models.ManyToManyField(to="product_module.product")),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
    ]
