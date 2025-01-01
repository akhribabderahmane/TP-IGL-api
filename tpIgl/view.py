from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from users.serializers import LoginSerializer, UserSerializer
from patients.serializers import PatientSerializer
from patients.models import Patient

@api_view(['POST'])
def login(request):
    serializer = LoginSerializer(data=request.data)
    if serializer.is_valid():
        user = serializer.validated_data["user"]
        if user.role == 'patient':
            patient = Patient.objects.get(user=user)
            response_data = PatientSerializer(patient).data
            response_data['user']['role'] = user.role
        else:
            response_data = UserSerializer(user).data
        return Response(response_data, status=status.HTTP_200_OK)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)