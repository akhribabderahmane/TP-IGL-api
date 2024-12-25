from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Patient, Dpi
from .serializers import PatientSerializer, DpiSerializer
from rest_framework.permissions import IsAuthenticated

class PatientViewSet(viewsets.ModelViewSet):
    #permission_classes = [IsAuthenticated]
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer
    
    @action(detail=False, methods=['get'])
    def search_by_nss(self, request):
        nss = request.query_params.get('nss', None)
        if nss is None:
            return Response(
                {"error": "NSS parameter is required"}, 
                status=status.HTTP_400_BAD_REQUEST
            )
            
        try:
            patient = Patient.objects.get(nss=nss)
            serializer = self.get_serializer(patient)
            return Response(serializer.data)
        except Patient.DoesNotExist:
            return Response(
                {"error": "Patient not found"}, 
                status=status.HTTP_404_NOT_FOUND
            )
    
    def destroy(self, request, *args, **kwargs):
        patient = self.get_object()
        # Delete the associated user as well
        patient.user.delete()  # This will cascade delete the patient
        return Response(status=status.HTTP_204_NO_CONTENT)
    

class DpiViewSet(viewsets.ModelViewSet):
    queryset = Dpi.objects.all()
    serializer_class = DpiSerializer

