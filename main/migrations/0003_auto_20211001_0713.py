# Generated by Django 3.2.5 on 2021-10-01 04:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_product_new'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='description_title',
        ),
        migrations.RemoveField(
            model_name='product',
            name='image2',
        ),
        migrations.RemoveField(
            model_name='product',
            name='image3',
        ),
        migrations.RemoveField(
            model_name='product',
            name='image4',
        ),
    ]