from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Soin
from consultations.models import Consultation
from .serializers import SoinSerializer


class SoinViewSet(viewsets.ModelViewSet):
    """
    ViewSet for managing Soins.
    """
    queryset = Soin.objects.all()
    serializer_class = SoinSerializer

    @action(detail=True, methods=['get'])
    def soins_for_consultation(self, request, pk=None):
        """
        Retrieve all soins for a specific consultation.
        """
        try:
            consultation = Consultation.objects.get(pk=pk)
        except Consultation.DoesNotExist:
            return Response(
                {"error": "Consultation not found"},
                status=status.HTTP_404_NOT_FOUND
            )

        soins = consultation.soins.all()
        serializer = SoinSerializer(soins, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
