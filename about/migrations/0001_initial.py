# Generated by Django 3.2 on 2022-02-07 21:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32)),
                ('description', models.TextField(blank=True)),
                ('price', models.DecimalField(decimal_places=2, max_digits=6)),
                ('slug', models.SlugField(max_length=48)),
                ('active', models.BooleanField(default=True)),
                ('in_Stock', models.BooleanField(default=True)),
                ('date_Updated', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='ProductTag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32)),
                ('slug', models.SlugField(max_length=48)),
                ('description', models.TextField(blank=True)),
                ('active', models.BooleanField(default=True)),
                ('product', models.ManyToManyField(blank=True, to='about.Product')),
            ],
        ),
        migrations.CreateModel(
            name='ProductImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='product-images')),
                ('thumbnail', models.ImageField(null=True, upload_to='product-thumbnails')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='about.product')),
            ],
        ),
    ]
