from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Consultation, Ordonnance, Medicament, Validation
from examinations.models import Examen
from patients.models import Dpi, Patient
from .serializers import ConsultationSerializer, OrdonnanceSerializer, MedicamentSerializer, DpiSerializer

class DpiViewSet(viewsets.ModelViewSet):
    queryset = Dpi.objects.all()
    serializer_class = DpiSerializer

    @action(detail=True, methods=['get'])
    def consultations(self, request, pk=None):
        dpi = self.get_object()
        consultations = dpi.consultations.all()
        serializer = ConsultationSerializer(consultations, many=True)
        return Response(serializer.data)

class OrdonnanceViewSet(viewsets.ModelViewSet):
    queryset = Ordonnance.objects.all()
    serializer_class = OrdonnanceSerializer

    @action(detail=True, methods=['patch'])
    def validate(self, request, pk=None):
        """Endpoint to validate the ordonnance."""
        ordonnance = self.get_object()
        if ordonnance.validation:
            ordonnance.validation.valid_state = True
            ordonnance.validation.save()
            return Response(
                {"message": "Ordonnance validated successfully", "valid_state": True},
                status=status.HTTP_200_OK,
            )
        return Response(
            {"error": "Validation object does not exist for this ordonnance"},
            status=status.HTTP_400_BAD_REQUEST,
        )


class ConsultationViewSet(viewsets.ModelViewSet):
    queryset = Consultation.objects.all()
    serializer_class = ConsultationSerializer

    @action(detail=False, methods=['get'])
    def by_patient(self, request):
        """Get the list of consultations by patient ID."""
        patient_id = request.query_params.get('patient_id', None)
        if not patient_id:
            return Response(
                {"error": "patient_id parameter is required"},
                status=status.HTTP_400_BAD_REQUEST,
            )
        
        try:
            # Fetch the Patient record using the provided patient_id
            patient = Patient.objects.get(pk=patient_id)
        except Patient.DoesNotExist:
            return Response(
                {"error": "No patient found for the given ID"},
                status=status.HTTP_404_NOT_FOUND,
            )

        # Access the patient's DPI
        dpi = patient.dpi

        # Get consultations associated with the DPI
        consultations = dpi.consultations.all()  # Assuming consultations are related to DPI
        serializer = self.get_serializer(consultations, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    

class MedicamentViewSet(viewsets.ModelViewSet):
    queryset = Medicament.objects.all()
    serializer_class = MedicamentSerializer
