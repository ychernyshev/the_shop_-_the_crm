# Generated by Django 4.2.4 on 2023-09-24 08:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('example__simple_admin', '0003_rename_at_stock_productmodel_in_stock_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productmodel',
            name='in_stock',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
    ]