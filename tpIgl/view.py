from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from users.serializers import LoginSerializer, UserSerializer

@api_view(['POST'])
def login(request):
    serializer = LoginSerializer(data=request.data)
    if serializer.is_valid():
        user = serializer.validated_data["user"]
        response_data = UserSerializer(user).data
        return Response(response_data, status=status.HTTP_200_OK)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)