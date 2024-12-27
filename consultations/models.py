from django.db import models
from patients.models import Dpi

# Create your models here.

class Validation(models.Model):
    data_validation = models.JSONField(default=dict, blank=True)  # Optional data
    valid_state = models.BooleanField(default=False)

class Ordonnance(models.Model):
    validation = models.OneToOneField(Validation, on_delete=models.SET_NULL, null=True, blank=True)

class Medicament(models.Model):
    ordonnance = models.ForeignKey(Ordonnance, on_delete=models.CASCADE, related_name="medicaments")
    nom = models.CharField(max_length=100)
    dose = models.IntegerField()
    duree = models.IntegerField()

class Consultation(models.Model):
    dpi = models.ForeignKey(Dpi, on_delete=models.CASCADE, related_name="consultations")
    date = models.DateField()
    diagnostic = models.TextField()
    ordonnance = models.OneToOneField(Ordonnance, on_delete=models.SET_NULL, null=True, blank=True)
    resume = models.TextField(null=True, blank=True)



