from django.db import models

# Create your models here.
class UserRole(models.TextChoices):
    ADMIN = "admin", "Admin"
    MEDECIN = "medecin", "Medecin"
    PHARMACIE = "pharmacie", "Pharmacie"
    INFIRMIER = "infermier", "Infermier"
    LABORATIN = "laboratin", "Laboratin"
    RADIOLOGUE = "radiologue", "Radiologue"


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

class Patient(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    nss = models.CharField(max_length=14,unique=True)
    date_naissance = models.DateField()
    addresse = models.CharField(max_length=100)
    mutuelle = models.TextField()
    medcin_traitant = models.ForeignKey(Medcin, on_delete=models.CASCADE)
    personne_contact = models.CharField(max_length=12, null=True, blank=True)
    dpi = models.OneToOneField('Dpi', on_delete=models.CASCADE)

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

class Dpi(models.Model):
    created_at = models.DateField(auto_now_add=True)
    antecedants = models.TextField(null=True, blank=True)
    bilan_biologique = models.TextField(null=True, blank=True)

class Consultation(models.Model):
    dpi = models.ForeignKey(Dpi, on_delete=models.CASCADE)
    date = models.DateField()
    diagnostic = models.TextField()
    ordonnance = models.OneToOneField('Ordonnance', on_delete=models.SET_NULL, null=True, blank=True)
    resume = models.TextField(null=True, blank=True)

class Ordonnance(models.Model):
    validation = models.OneToOneField('Validation', on_delete=models.SET_NULL, null=True, blank=True)

class Examen(models.Model):
    consultation = models.ForeignKey(Consultation, on_delete=models.CASCADE)
    laborantin = models.ForeignKey(Laboratin, on_delete=models.SET_NULL, null=True, blank=True)
    radiologue = models.ForeignKey(Radiologue, on_delete=models.SET_NULL, null=True, blank=True)
    type_examen = models.CharField(max_length=100)
    compte_rendu = models.OneToOneField('CompteRendu', on_delete=models.SET_NULL, null=True, blank=True)

class Soin(models.Model):
    consultation = models.ForeignKey(Consultation, on_delete=models.CASCADE)
    infermier = models.ForeignKey(Infermie, on_delete=models.CASCADE)
    data_soin = models.JSONField()
    type_soin = models.CharField(max_length=100)
    etat_patient = models.CharField(max_length=100)
    observation = models.CharField(max_length=100, null=True, blank=True)

class Medicament(models.Model):
    ordonnance = models.ForeignKey(Ordonnance, on_delete=models.CASCADE)
    nom = models.CharField(max_length=100)
    dose = models.IntegerField()
    duree = models.IntegerField()

class Validation(models.Model):
    data_validation = models.JSONField()
    valid_state = models.BooleanField(default=False)

class CompteRendu(models.Model):
    contenu = models.TextField(default="")
    resultat = models.TextField()
    fichier_upload = models.CharField(max_length=1000, null=True, blank=True)

