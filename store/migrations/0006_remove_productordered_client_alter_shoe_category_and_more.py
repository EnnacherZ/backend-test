# Generated by Django 5.1.2 on 2024-11-03 14:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0005_productordered'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='productordered',
            name='client',
        ),
        migrations.AlterField(
            model_name='shoe',
            name='category',
            field=models.CharField(choices=[('Mocassin', 'Mocassin'), ('Basket', 'Basket'), ('Medical', 'Medical'), ('Classic', 'Classic')], max_length=100),
        ),
        migrations.DeleteModel(
            name='Client',
        ),
        migrations.DeleteModel(
            name='ProductOrdered',
        ),
    ]