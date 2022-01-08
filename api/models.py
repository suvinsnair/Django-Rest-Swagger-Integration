from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from decimal import Decimal

# Create your models here.

class AcConfig(models.Model):
    target_temp = models.DecimalField(max_digits=6, decimal_places=3, default=0,
    validators=[MinValueValidator(Decimal('5.000')), MaxValueValidator(Decimal('20.000'))])
    target_humidity = models.DecimalField(max_digits=6, decimal_places=3, default=0,
    validators=[MinValueValidator(Decimal('5.000')), MaxValueValidator(Decimal('20.000'))])
    name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name