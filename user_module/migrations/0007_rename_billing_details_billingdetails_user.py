# Generated by Django 4.2.3 on 2023-12-29 11:23

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("user_module", "0006_remove_customuser_billing_details_and_more"),
    ]

    operations = [
        migrations.RenameField(
            model_name="billingdetails",
            old_name="billing_details",
            new_name="user",
        ),
    ]
