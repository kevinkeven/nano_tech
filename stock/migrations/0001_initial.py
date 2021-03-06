# Generated by Django 3.2.4 on 2021-07-14 16:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ProductType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=200)),
                ('slug', models.SlugField(max_length=200, unique=True)),
            ],
            options={
                'verbose_name_plural': 'products_type',
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=250)),
                ('image', models.ImageField(blank=True, upload_to='product/%Y/%m/%d')),
                ('slug', models.SlugField(blank=True, max_length=250, unique=True)),
                ('desc', models.TextField()),
                ('price', models.PositiveIntegerField()),
                ('disc_price', models.PositiveIntegerField(blank=True, null=True)),
                ('specs', models.TextField(null=True)),
                ('available', models.BooleanField(default=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('prec', models.IntegerField(blank=True, null=True)),
                ('product_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='products', to='stock.producttype')),
            ],
            options={
                'ordering': ('name',),
                'index_together': {('id', 'slug')},
            },
        ),
    ]
