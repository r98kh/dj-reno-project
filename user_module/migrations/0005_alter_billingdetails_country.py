# Generated by Django 4.2.3 on 2023-12-29 09:33

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("user_module", "0004_billingdetails_customuser_billing_details"),
    ]

    operations = [
        migrations.AlterField(
            model_name="billingdetails",
            name="Country",
            field=models.CharField(choices=[("1", "ایران")], max_length=50),
        ),
    ]
