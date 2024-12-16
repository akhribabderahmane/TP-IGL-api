from django.db import models
from users.models import User,Medcin
# Create your models here.

class Patient(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    nss = models.CharField(max_length=14,unique=True)
    date_naissance = models.DateField()
    addresse = models.CharField(max_length=100)
    mutuelle = models.TextField()
    medcin_traitant = models.ForeignKey(Medcin, on_delete=models.CASCADE)
    personne_contact = models.CharField(max_length=12, null=True, blank=True)
    dpi = models.OneToOneField('Dpi', on_delete=models.CASCADE)
    
class Dpi(models.Model):
    created_at = models.DateField(auto_now_add=True)
    antecedants = models.TextField(null=True, blank=True)
    bilan_biologique = models.TextField(null=True, blank=True)

