# Generated by Django 3.2.5 on 2021-09-19 05:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_auto_20210919_0816'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='received_on',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
