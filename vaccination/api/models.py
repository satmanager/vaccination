from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
# Create your models here.

class Drug(models.Model):
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=10)
    description = models.CharField(max_length=255)
    def __str__(self):
        return self.name

class Vaccination(models.Model):
    rut = models.CharField(max_length=9)
    dose = models.FloatField(validators=[MinValueValidator(0.15),MaxValueValidator(1.0)])
    date = models.DateField()
    drug = models.ForeignKey(Drug, related_name='drugs', on_delete=models.RESTRICT)
    def __str__(self):
        return self.name        