# Generated by Django 3.2.3 on 2022-07-16 15:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0016_sales_salesitems'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sales',
            name='date',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
