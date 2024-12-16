from django.db import models
from consultations.models import Consultation
from users.models import Laboratin,Radiologue

# Create your models here.

class Examen(models.Model):
    consultation = models.ForeignKey(Consultation, on_delete=models.CASCADE)
    laborantin = models.ForeignKey(Laboratin, on_delete=models.SET_NULL, null=True, blank=True)
    radiologue = models.ForeignKey(Radiologue, on_delete=models.SET_NULL, null=True, blank=True)
    type_examen = models.CharField(max_length=100)
    compte_rendu = models.OneToOneField('CompteRendu', on_delete=models.SET_NULL, null=True, blank=True)
    
class CompteRendu(models.Model):
    contenu = models.TextField(default="")
    resultat = models.TextField()
    fichier_upload = models.CharField(max_length=1000, null=True, blank=True)
