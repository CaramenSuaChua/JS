# Generated by Django 4.1.4 on 2022-12-16 04:18

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.CharField(max_length=150)),
                ('pin_code', models.CharField(max_length=10)),
                ('city', models.CharField(max_length=50)),
                ('paid', models.BooleanField(default=False)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('status', models.CharField(choices=[('Pending', 'Pending'), ('Packed', 'Packed'), ('Shipped', 'Shipped'), ('Delivered', 'Delivered')], default='Pending', max_length=10)),
                ('total_price', models.FloatField()),
                ('phone', models.CharField(max_length=100, null=True)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='pro_order', to='products.products')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='order_user', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ('-created', 'id'),
            },
        ),
        migrations.CreateModel(
            name='OrderItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.PositiveIntegerField(default=1)),
                ('total', models.FloatField()),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='item', to='orders.order')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='order_pro', to='products.products')),
            ],
        ),
    ]
