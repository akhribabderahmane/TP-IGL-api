from django.db import models
from users.models import Infermie
from consultations.models import Consultation


class Soin(models.Model):
    consultation = models.ForeignKey(Consultation, on_delete=models.CASCADE)
    infermier = models.ForeignKey(Infermie, on_delete=models.CASCADE)
    type_soin = models.CharField(max_length=100)
    etat_patient = models.CharField(max_length=100)
    observation = models.CharField(max_length=100, null=True, blank=True)