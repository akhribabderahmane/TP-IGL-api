from django.db import models
from consultations.models import Consultation
from users.models import User  # Assuming User is the parent model for Laboratin and Radiologue

class CompteRendu(models.Model):
    contenu = models.TextField(default="")
    resultat = models.TextField()
    fichier_upload = models.CharField(max_length=1000, null=True, blank=True)

class Examen(models.Model):
    EXAMEN_TYPE_CHOICES = [
        ('biologique', 'Biologique'),
        ('radiologique', 'Radiologique'),
    ]

    consultation = models.ForeignKey(Consultation, on_delete=models.CASCADE)
    technicien = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    type_examen = models.CharField(max_length=20, choices=EXAMEN_TYPE_CHOICES)
    compte_rendu = models.OneToOneField(CompteRendu, on_delete=models.SET_NULL, null=True, blank=True)
