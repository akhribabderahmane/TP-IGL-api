from django.db import models

# Create your models here.
class UserRole(models.TextChoices):
    ADMIN = "admin", "Admin"
    MEDECIN = "medecin", "Medecin"
    PHARMACIE = "pharmacie", "Pharmacie"
    INFIRMIER = "infermier", "Infermier"
    LABORATIN = "laboratin", "Laboratin"
    RADIOLOGUE = "radiologue", "Radiologue"
    PATIENT = "patient", "Patient"


class User(models.Model):
    nom = models.CharField(max_length=100)
    prenom = models.CharField(max_length=100)
    telephone = models.CharField(max_length=12)
    email = models.EmailField(max_length=100,unique=True)
    password = models.CharField(max_length=128)
    role = models.CharField(max_length=20, choices=UserRole.choices)
    
class Admin(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

class Medcin(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    specialite = models.CharField(max_length=100)

class Pharmacie(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

class Infermie(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

class Laboratin(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    specialite = models.CharField(max_length=100)

class Radiologue(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    specialite = models.CharField(max_length=100)