# Generated by Django 4.1.4 on 2022-12-13 01:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='order',
            options={'ordering': ('-created', 'id')},
        ),
        migrations.RenameField(
            model_name='order',
            old_name='products',
            new_name='product',
        ),
    ]