# Generated by Django 4.1.4 on 2022-12-13 01:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_products_description_alter_products_price_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='products',
            options={'ordering': ('id',)},
        ),
    ]