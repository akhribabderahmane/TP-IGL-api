from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Consultation, Ordonnance, Medicament, Validation
from patients.models import Dpi
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

    def create(self, request, *args, **kwargs):
        """
        Overriding the create method to:
        - Create a new consultation.
        - Automatically assign an empty ordonnance to it.
        """
        # Extract consultation data
        consultation_data = request.data
        dpi_id = consultation_data.get("dpi")

        try:
            # Validate DPI existence
            dpi = Dpi.objects.get(pk=dpi_id)
        except Dpi.DoesNotExist:
            return Response({"error": "DPI not found"}, status=status.HTTP_404_NOT_FOUND)

        # Create Consultation
        serializer = self.get_serializer(data=consultation_data)
        serializer.is_valid(raise_exception=True)
        consultation = serializer.save(dpi=dpi)

        # Automatically create empty ordonnance with validation
        validation = Validation.objects.create(data_validation={}, valid_state=False)
        ordonnance = Ordonnance.objects.create(validation=validation)

        # Assign ordonnance to the consultation
        consultation.ordonnance = ordonnance
        consultation.save()

        return Response(self.get_serializer(consultation).data, status=status.HTTP_201_CREATED)

class MedicamentViewSet(viewsets.ModelViewSet):
    queryset = Medicament.objects.all()
    serializer_class = MedicamentSerializer
