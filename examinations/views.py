from rest_framework import viewsets, status
from rest_framework.response import Response
from .models import Examen, CompteRendu
from .serializers import ExamenSerializer, CompteRenduSerializer

class ExamenViewSet(viewsets.ModelViewSet):
    queryset = Examen.objects.all()
    serializer_class = ExamenSerializer

    def create(self, request, *args, **kwargs):
        """Create a new Examen with optional CompteRendu."""
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        examen = serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
