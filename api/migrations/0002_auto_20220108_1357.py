# Generated by Django 3.2.11 on 2022-01-08 08:27

from decimal import Decimal
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='acconfig',
            name='target_humidity',
            field=models.DecimalField(decimal_places=3, default=0, max_digits=6, validators=[django.core.validators.MinValueValidator(Decimal('5.000')), django.core.validators.MaxValueValidator(Decimal('20.000'))]),
        ),
        migrations.AlterField(
            model_name='acconfig',
            name='target_temp',
            field=models.DecimalField(decimal_places=3, default=0, max_digits=6, validators=[django.core.validators.MinValueValidator(Decimal('5.000')), django.core.validators.MaxValueValidator(Decimal('20.000'))]),
        ),
    ]