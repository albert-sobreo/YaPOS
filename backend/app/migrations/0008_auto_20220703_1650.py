# Generated by Django 3.2.3 on 2022-07-03 16:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_receivingreport_suppliers'),
    ]

    operations = [
        migrations.AlterField(
            model_name='receivingreportitems',
            name='inventory',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='rritems', to='app.inventory'),
        ),
        migrations.AlterField(
            model_name='receivingreportitems',
            name='rr',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='rritems', to='app.receivingreport'),
        ),
    ]
