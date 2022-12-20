# Generated by Django 4.1.4 on 2022-12-20 01:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
        ('orders', '0004_remove_order_products_remove_orderitem_product_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='address',
            field=models.CharField(blank=True, max_length=150, null=True),
        ),
        migrations.AlterField(
            model_name='order',
            name='order_item',
            field=models.ManyToManyField(to='orders.orderitem', verbose_name='items'),
        ),
        migrations.AlterField(
            model_name='orderitem',
            name='product',
            field=models.ManyToManyField(related_name='orders', to='products.products'),
        ),
    ]
