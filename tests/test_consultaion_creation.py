import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "tpIgl.settings")

import django
django.setup()

from django.core.management import call_command

import pytest
from consultations.models import Consultation, Ordonnance, Validation
from examinations.models import Examen
from patients.models import Dpi
from users.models import  Laboratin, User

@pytest.mark.django_db
def test_create_consultation_with_ordonnance_and_examen():
    # Create a test DPI
    dpi = Dpi.objects.create()  # Assuming patient ID 1 exists

    # Create consultation
    consultation_data = {
        'dpi': dpi,
        'date': '2024-12-27',
        'diagnostic': 'Test Diagnostic',
        'resume': 'Test Resume',
    }
    consultation = Consultation.objects.create(**consultation_data)

    # Automatically create an ordonnance
    validation = Validation.objects.create(valid_state=False)
    ordonnance = Ordonnance.objects.create(validation=validation)

    # Assign ordonnance to consultation
    consultation.ordonnance = ordonnance
    consultation.save()

    # Create an examen for the consultation

    laboratin = User.objects.create()  # Assuming a valid Laboratin exists

    examen_data = {
        'consultation': consultation,
        'technicien': laboratin,
        'type_examen': 'radiologique',
    }
    examen = Examen.objects.create(**examen_data)

    # Check if the examen is correctly assigned to the consultation
    assert consultation.examen_set.count() == 1

    # Clean up
    consultation.delete()
    ordonnance.delete()
    examen.delete()
    laboratin.delete()

