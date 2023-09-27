# Generated by Django 4.2.4 on 2023-09-16 20:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('example__simple_admin', '0002_productmodel_main_image'),
    ]

    operations = [
        migrations.RenameField(
            model_name='productmodel',
            old_name='at_stock',
            new_name='in_stock',
        ),
        migrations.CreateModel(
            name='AdditionalImageModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='products/')),
                ('parent_model', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='product_additional_image', to='example__simple_admin.productmodel')),
            ],
            options={
                'verbose_name': ('product',),
                'verbose_name_plural': 'Products',
            },
        ),
    ]