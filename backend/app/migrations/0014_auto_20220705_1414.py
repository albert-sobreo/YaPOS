# Generated by Django 3.2.3 on 2022-07-05 14:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0013_auto_20220705_1413'),
    ]

    operations = [
        migrations.AlterField(
            model_name='adjustment',
            name='date',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='receivingreport',
            name='date',
            field=models.DateTimeField(),
        ),
    ]
