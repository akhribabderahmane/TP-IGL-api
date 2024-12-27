from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Consultation, Ordonnance, Medicament, Validation
from examinations.models import Examen
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

    @action(detail=True, methods=['post'])
    def add_examen(self, request, pk=None):
        """Add an Examen to a specific consultation."""
        consultation = self.get_object()
        examen_data = request.data

        # Validate and create the Examen
        serializer = ExamenSerializer(data=examen_data)
        serializer.is_valid(raise_exception=True)
        examen = serializer.save(consultation=consultation)

        return Response(ExamenSerializer(examen).data, status=status.HTTP_201_CREATED)
    

class MedicamentViewSet(viewsets.ModelViewSet):
    queryset = Medicament.objects.all()
    serializer_class = MedicamentSerializer
