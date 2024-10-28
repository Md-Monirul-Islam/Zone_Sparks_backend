from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.contrib.auth import authenticate
from django.contrib.auth import get_user_model
from .models import Account
from .serializers import AccountSerializer
from django.contrib.auth import logout

User = get_user_model()

@api_view(['POST'])
def signup(request):
    data = request.data
    email = data.get('email')
    password = data.get('password')
    
    if User.objects.filter(email=email).exists():
        return Response({'error': 'Email is already in use.'}, status=status.HTTP_400_BAD_REQUEST)

    user = User.objects.create_user(email=email, password=password)
    
    return Response({
        'message': 'User created successfully',
        'user_id': user.id,
        'email': user.email
    }, status=status.HTTP_201_CREATED)



@api_view(['POST'])
def login(request):
    data = request.data
    email = data.get('email')
    password = data.get('password')
    
    user = authenticate(request, username=email, password=password)
    
    if user is not None:
        # Here, you can generate tokens if you're using JWT
        return Response({
            'message': 'Login successful',
            'user_id': user.id,
            'email': user.email,
            # Include token if using JWT
        }, status=status.HTTP_200_OK)
    else:
        return Response({'error': 'Invalid email or password'}, status=status.HTTP_400_BAD_REQUEST)



@api_view(['POST'])
def logout_view(request):
    logout(request)  # This will clear the session
    return Response({"message": "Logout successful"}, status=status.HTTP_200_OK)