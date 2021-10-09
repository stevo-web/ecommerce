# Generated by Django 3.2.5 on 2021-10-05 04:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_auto_20211001_2233'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='estimated',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('pending', 'pending'), ('in Transit', 'in Transit'), ('delivered', 'delivered')], max_length=20),
        ),
    ]