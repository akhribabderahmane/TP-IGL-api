from rest_framework import serializers
from .models import Consultation, Ordonnance, Medicament, Validation
from care.models import Soin  # Import the Soin model
from examinations.models import Examen
from examinations.serializers import ExamenSerializer  # Import the ExamenSerializer
from patients.models import Dpi

class SoinSerializer(serializers.ModelSerializer):
    """Serializer for Soin model."""
    class Meta:
        model = Soin
        fields = ['id', 'type_soin', 'etat_patient', 'observation', 'infermier']

class ValidationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Validation
        fields = "__all__"

class MedicamentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Medicament
        fields = "__all__"

class OrdonnanceSerializer(serializers.ModelSerializer):
    medicaments = MedicamentSerializer(many=True, read_only=True)  # Include related medicaments

    class Meta:
        model = Ordonnance
        fields = "__all__"


class ConsultationSerializer(serializers.ModelSerializer):
    ordonnance = OrdonnanceSerializer(read_only=True)  # Include related ordonnance
    soins = SoinSerializer(many=True, read_only=True)  # Include related soins
    examens = ExamenSerializer(many=True, read_only=True, source="examen_set")  # Include related examens

    class Meta:
        model = Consultation
        fields = "__all__"


class DpiSerializer(serializers.ModelSerializer):
    consultations = ConsultationSerializer(many=True, read_only=True)

    class Meta:
        model = Dpi
        fields = '__all__'
