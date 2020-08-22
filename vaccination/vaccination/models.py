# models.py
from django.db import models
class Drug(models.Model):
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=10)
    description = models.CharField(max_length=255)
    def __str__(self):
        return self.name

class Vaccination(models.Model):
    rut = models.CharField(max_length=8)
    dose = models.FloatField(min=0.15, max=1.0)
    date = models.DateField()
    drug = models.ForeignKey(Drug)
    def __str__(self):
        return self.name        