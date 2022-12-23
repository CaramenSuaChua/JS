# Generated by Django 4.1.4 on 2022-12-21 09:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Consult',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=25)),
                ('position', models.CharField(blank=True, max_length=25, null=True)),
                ('group', models.CharField(max_length=50)),
                ('email', models.CharField(blank=True, max_length=25, null=True)),
                ('phone', models.CharField(blank=True, max_length=25, null=True)),
                ('describe', models.TextField(blank=True, null=True)),
                ('file', models.FileField(blank=True, null=True, upload_to='')),
                ('create_date', models.DateTimeField(auto_now_add=True)),
                ('update_date', models.DateTimeField(auto_now=True)),
            ],
            options={
                'db_table': 'Consult',
            },
        ),
    ]