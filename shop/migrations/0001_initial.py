# Generated by Django 5.1.6 on 2025-02-21 07:51

import django.db.models.deletion
import shop.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Catagory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=150)),
                ('image', models.ImageField(blank=True, null=True, upload_to=shop.models.getfilename)),
                ('descrpiton', models.TextField(max_length=500)),
                ('status', models.BooleanField(default=False, help_text='0-default,1-hidden')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('vendor', models.CharField(max_length=150)),
                ('product_image', models.ImageField(blank=True, null=True, upload_to=shop.models.getfilename)),
                ('quantitiy', models.IntegerField()),
                ('original_price', models.FloatField()),
                ('selling_price', models.IntegerField()),
                ('descrpition', models.TextField(max_length=500)),
                ('status', models.BooleanField(default=False, help_text='0-defalut,1-hidden')),
                ('trending', models.BooleanField(default=False, help_text='0-defalut,1-trending')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.catagory')),
            ],
        ),
    ]
