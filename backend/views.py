from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

@api_view(['GET'])
def helloworld(request):
    data = {
        'message': "UwU",
        'content': "idk what else",
        'url': "https://example.com",
    }
    return Response(data)

@api_view(['POST'])
def login_user(request):
    # Process user login logic here
    return Response({'message': 'User logged in successfully.'}, status=status.HTTP_200_OK)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def logout_user(request):
    # Process user logout logic here
    return Response({'message': 'User logged out successfully.'}, status=status.HTTP_200_OK)
