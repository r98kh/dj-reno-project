# Generated by Django 4.2.3 on 2023-07-15 06:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product_module', '0003_productcomments'),
    ]

    operations = [
        migrations.DeleteModel(
            name='ProductComments',
        ),
    ]
