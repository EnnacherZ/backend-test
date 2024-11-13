# Generated by Django 5.1.2 on 2024-10-23 21:17

import django.db.models.deletion
import phonenumber_field.modelfields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_id', models.CharField(max_length=100)),
                ('transaction_id', models.CharField(max_length=100)),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('phone', phonenumber_field.modelfields.PhoneNumberField(max_length=128, region=None)),
                ('city', models.CharField(max_length=50)),
                ('address', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='ProductOrdered',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_type', models.CharField(max_length=50)),
                ('size', models.CharField(max_length=20)),
                ('quantity', models.PositiveIntegerField()),
                ('category', models.CharField(max_length=50)),
                ('ref', models.CharField(max_length=50)),
                ('name', models.CharField(max_length=50)),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='store.client')),
            ],
        ),
    ]
