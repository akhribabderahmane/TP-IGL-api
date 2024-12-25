from django.db import models
from users.models import User, Medcin

class Dpi(models.Model):
    created_at = models.DateField(auto_now_add=True)
    antecedants = models.TextField(null=True, blank=True)
    bilan_biologique = models.TextField(null=True, blank=True)

    def __str__(self):
        return f"DPI {self.pk}"

class Patient(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    nss = models.CharField(max_length=14, unique=True)
    date_naissance = models.DateField()
    addresse = models.CharField(max_length=100)
    mutuelle = models.TextField()
    medcin_traitant = models.ForeignKey(Medcin, on_delete=models.SET_NULL, null=True, blank=True)  # Optional doctor
    personne_contact = models.CharField(max_length=12, null=True, blank=True)
    dpi = models.OneToOneField(Dpi, on_delete=models.CASCADE)

    def __str__(self):
        return f"Patient {self.user.nom} {self.user.prenom}"
