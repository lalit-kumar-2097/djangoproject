# Generated by Django 2.2.1 on 2019-05-17 19:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0005_remove_product_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='image',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
    ]