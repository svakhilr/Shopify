# Generated by Django 4.1.5 on 2023-01-29 11:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_name', models.CharField(max_length=50, unique=True)),
                ('slug', models.SlugField(unique=True)),
                ('description', models.TextField(blank=True, max_length=200)),
                ('cat_img', models.ImageField(upload_to='catog_img')),
            ],
            options={
                'verbose_name': 'catagory',
                'verbose_name_plural': 'catagories',
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(max_length=100, unique=True)),
                ('slug', models.SlugField(unique=True)),
                ('price', models.IntegerField()),
                ('description', models.TextField(blank=True, max_length=500)),
                ('images', models.ImageField(null=True, upload_to='photos/products')),
                ('images1', models.ImageField(null=True, upload_to='photos/products')),
                ('images2', models.ImageField(null=True, upload_to='photos/products')),
                ('images3', models.ImageField(null=True, upload_to='photos/products')),
                ('stock', models.IntegerField()),
                ('is_available', models.BooleanField(default=True)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('modified_date', models.DateTimeField(auto_now=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='store.category')),
            ],
        ),
        migrations.CreateModel(
            name='Variation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('variation_category', models.CharField(choices=[('size', 'size')], max_length=100)),
                ('variation_value', models.CharField(max_length=7)),
                ('is_active', models.BooleanField(default=True)),
                ('created_date', models.DateField(auto_now=True)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='store.product')),
            ],
        ),
    ]
