# Generated by Django 5.0.1 on 2024-04-28 08:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projectstructure', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='image',
        ),
        migrations.RemoveField(
            model_name='product',
            name='quantity',
        ),
    ]