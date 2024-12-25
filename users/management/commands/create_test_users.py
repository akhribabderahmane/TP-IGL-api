from django.core.management.base import BaseCommand
from users.models import (
    User, Admin, Medcin, Pharmacie, 
    Infermie, Laboratin, Radiologue
)

class Command(BaseCommand):
    help = 'Creates test users for different roles'

    def handle(self, *args, **kwargs):
        self.stdout.write('Creating test users...')

        # Create Admin
        admin_user = User.objects.create(
            nom="Admin",
            prenom="Test",
            telephone="0123456789",
            email="admin@test.com",
            password="adminpass123",
            role="admin"
        )
        Admin.objects.create(user=admin_user)
        self.stdout.write(self.style.SUCCESS(f'Created Admin: {admin_user.email}'))

        # Create 2 Medecins
        medecin_data = [
            {
                'nom': 'Docteur',
                'prenom': 'One',
                'telephone': '0123456781',
                'email': 'doctor1@test.com',
                'specialite': 'Cardiologue'
            },
            {
                'nom': 'Docteur',
                'prenom': 'Two',
                'telephone': '0123456782',
                'email': 'doctor2@test.com',
                'specialite': 'Généraliste'
            }
        ]

        for data in medecin_data:
            medecin_user = User.objects.create(
                nom=data['nom'],
                prenom=data['prenom'],
                telephone=data['telephone'],
                email=data['email'],
                password="medecinpass123",
                role="medecin"
            )
            Medcin.objects.create(
                user=medecin_user,
                specialite=data['specialite']
            )
            self.stdout.write(self.style.SUCCESS(f'Created Medecin: {medecin_user.email}'))

        # Create Pharmacien
        pharmacien_user = User.objects.create(
            nom="Pharmacien",
            prenom="Test",
            telephone="0123456783",
            email="pharmacien@test.com",
            password="pharmapass123",
            role="pharmacie"
        )
        Pharmacie.objects.create(user=pharmacien_user)
        self.stdout.write(self.style.SUCCESS(f'Created Pharmacien: {pharmacien_user.email}'))

        # Create Infirmier
        infirmier_user = User.objects.create(
            nom="Infirmier",
            prenom="Test",
            telephone="0123456784",
            email="infirmier@test.com",
            password="infirmierpass123",
            role="infermier"
        )
        Infermie.objects.create(user=infirmier_user)
        self.stdout.write(self.style.SUCCESS(f'Created Infirmier: {infirmier_user.email}'))

        # Create Laborantin
        laborantin_user = User.objects.create(
            nom="Laborantin",
            prenom="Test",
            telephone="0123456785",
            email="laborantin@test.com",
            password="labopass123",
            role="laboratin"
        )
        Laboratin.objects.create(
            user=laborantin_user,
            specialite="Biochimie"
        )
        self.stdout.write(self.style.SUCCESS(f'Created Laborantin: {laborantin_user.email}'))

        # Create Radiologue
        radiologue_user = User.objects.create(
            nom="Radiologue",
            prenom="Test",
            telephone="0123456786",
            email="radiologue@test.com",
            password="radiopass123",
            role="radiologue"
        )
        Radiologue.objects.create(
            user=radiologue_user,
            specialite="IRM"
        )
        self.stdout.write(self.style.SUCCESS(f'Created Radiologue: {radiologue_user.email}'))

        self.stdout.write(self.style.SUCCESS('Successfully created all test users'))