# Generated by Django 4.2.7 on 2024-05-20 02:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='discount',
            field=models.DecimalField(blank=True, decimal_places=2, default=0.0, max_digits=5, null=True, verbose_name='Descuento'),
        ),
    ]
