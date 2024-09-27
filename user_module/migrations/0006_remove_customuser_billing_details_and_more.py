# Generated by Django 4.2.3 on 2023-12-29 11:20

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("user_module", "0005_alter_billingdetails_country"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="customuser",
            name="billing_details",
        ),
        migrations.AddField(
            model_name="billingdetails",
            name="billing_details",
            field=models.OneToOneField(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to=settings.AUTH_USER_MODEL,
            ),
        ),
    ]
