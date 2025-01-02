from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import action
from .models import Medcin, User
from .serializers import DoctorSerializer, UserSerializer
from rest_framework.permissions import IsAuthenticated

class DoctorViewSet(viewsets.ModelViewSet):
    # Uncomment IsAuthenticated if authentication is required
    # permission_classes = [IsAuthenticated]
    queryset = Medcin.objects.all()
    serializer_class = DoctorSerializer

    @action(detail=True, methods=['get'])
    def details(self, request, pk=None):
        try:
            doctor = self.get_object()
            serializer = self.get_serializer(doctor)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Medcin.DoesNotExist:
            return Response(
                {"error": "Doctor not found"}, 
                status=status.HTTP_404_NOT_FOUND
            )

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
