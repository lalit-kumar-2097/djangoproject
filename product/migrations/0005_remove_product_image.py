# Generated by Django 2.2.1 on 2019-05-17 19:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0004_product_category'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='image',
        ),
    ]
