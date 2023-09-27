# Generated by Django 4.2.4 on 2023-09-14 16:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ProductModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('slug', models.CharField(max_length=50)),
                ('description', models.TextField()),
                ('price', models.FloatField()),
                ('at_stock', models.BooleanField(default=False)),
                ('count', models.IntegerField()),
            ],
            options={
                'verbose_name': ('product',),
                'verbose_name_plural': 'Products',
            },
        ),
    ]
