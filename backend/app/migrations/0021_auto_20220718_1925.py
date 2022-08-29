# Generated by Django 3.2.3 on 2022-07-18 19:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0020_auto_20220716_2130'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='adjustment',
            options={'verbose_name': 'Adjustment', 'verbose_name_plural': 'Adjustments'},
        ),
        migrations.AlterModelOptions(
            name='adjustmentitems',
            options={'verbose_name': 'Adjustment Item', 'verbose_name_plural': 'Adjustment Items'},
        ),
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name': 'Category', 'verbose_name_plural': 'Categories'},
        ),
        migrations.AlterModelOptions(
            name='customers',
            options={'verbose_name': 'Customer', 'verbose_name_plural': 'Customers'},
        ),
        migrations.AlterModelOptions(
            name='inventory',
            options={'verbose_name': 'Inventory', 'verbose_name_plural': 'Inventory'},
        ),
        migrations.AlterModelOptions(
            name='receivingreport',
            options={'verbose_name': 'Receiving Report', 'verbose_name_plural': 'Receiving Reports'},
        ),
        migrations.AlterModelOptions(
            name='receivingreportitems',
            options={'verbose_name': 'Receiving Report Item', 'verbose_name_plural': 'Receiving Report Items'},
        ),
        migrations.AlterModelOptions(
            name='sales',
            options={'verbose_name': 'Sale', 'verbose_name_plural': 'Sales'},
        ),
        migrations.AlterModelOptions(
            name='salesitems',
            options={'verbose_name': 'Sales Item', 'verbose_name_plural': 'Sales Items'},
        ),
        migrations.AlterModelOptions(
            name='suppliers',
            options={'verbose_name': 'Supplier', 'verbose_name_plural': 'Suppliers'},
        ),
        migrations.AlterModelOptions(
            name='testlist',
            options={'verbose_name': 'Test List', 'verbose_name_plural': 'Test List'},
        ),
        migrations.AddField(
            model_name='sales',
            name='void',
            field=models.BooleanField(default=False),
        ),
    ]
