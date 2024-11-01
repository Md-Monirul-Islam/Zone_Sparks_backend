# Generated by Django 5.1.2 on 2024-10-31 17:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store_app', '0004_product_quantity'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='quantity',
            new_name='total_sales',
        ),
        migrations.AlterField(
            model_name='stock',
            name='quantity',
            field=models.PositiveIntegerField(),
        ),
    ]
