# Generated by Django 4.2.3 on 2023-07-15 06:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('product_module', '0002_alter_productfeatures_product_productgallery'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProductComments',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('text', models.TextField()),
                ('demonstrable', models.BooleanField(default=True)),
                ('created_date', models.DateField(auto_now_add=True)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='product_module.product')),
            ],
        ),
    ]
