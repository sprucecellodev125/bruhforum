from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from .models import Core, Post, Comment

@api_view(['GET'])
def rootdir(request):
    allpost = Post.objects.all().order_by('-postdate').values()
    try:
        core = Core.objects.all().values
    except Core.DoesNotExist:
        core = None
    need_setup = Core.objects.values_list('needsetup', flat=True).first()
    about = Core.objects.values_list('about', flat=True).first()
    rules = Core.objects.values_list('rules', flat=True).first()
    name = Core.objects.values_list('name', flat=True).first()
    return Response(
        {
            'allpost': allpost,
            'needsetup': need_setup,
            'about': about,
            'rules': rules,
            'name': name,
        }
    )

@api_view(['POST'])
def login_user(request):
    # Process user login logic here
    return Response({'message': 'User logged in successfully.'}, status=status.HTTP_200_OK)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def logout_user(request):
    # Process user logout logic here
    return Response({'message': 'User logged out successfully.'}, status=status.HTTP_200_OK)
