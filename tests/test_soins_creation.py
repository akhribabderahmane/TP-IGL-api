import pytest
from consultations.models import Consultation, Ordonnance, Validation
from patients.models import Dpi
from care.models import Soin
from users.models import Infermie

@pytest.mark.django_db
def test_create_soin_and_add_to_consultation():
    # Create a test DPI and Consultation
    dpi = Dpi.objects.create()  # Assuming patient ID 1 exists
    consultation = Consultation.objects.create(
        dpi=dpi,
        date='2024-12-27',
        diagnostic='Test Diagnostic',
        resume='Test Resume'
    )

    # Create a soin for the consultation
    infermie = Infermie.objects.create(user_id=10)  # Assuming a valid Infermie exists

    soin_data = {
        'consultation': consultation,
        'infermier': infermie,
        'type_soin': 'Test Soin',
        'etat_patient': 'Stable',
        'observation': 'No issues observed'
    }
    soin = Soin.objects.create(**soin_data)

    # Check if the soin is correctly assigned to the consultation
    assert consultation.soin_set.count() == 1

    # Clean up
    soin.delete()
    consultation.delete()
    dpi.delete()
    infermie.delete()

