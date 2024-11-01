from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.contrib.auth import authenticate
from django.contrib.auth import get_user_model
from .models import Account, UserProfile
from .serializers import AccountSerializer, UserProfileSerializer
from django.contrib.auth import logout
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework import generics, permissions
from rest_framework_simplejwt.tokens import AccessToken
from rest_framework.permissions import AllowAny
from rest_framework.decorators import api_view, permission_classes

User = get_user_model()

@api_view(['POST'])
@permission_classes([AllowAny]) 
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
@permission_classes([AllowAny])
def login(request):
    data = request.data
    email = data.get('email')
    password = data.get('password')
    
    user = authenticate(username=email, password=password)
    
    if user is not None:
        access_token = AccessToken.for_user(user)
        
        response_data = {
            'message': 'Login successful',
            'user_id': user.id,
            'email': user.email,
            'token': str(access_token),
            'is_superuser': user.is_superuser  # Include superuser status
        }
        
        return Response(response_data, status=status.HTTP_200_OK)
    else:
        return Response({'error': 'Invalid email or password'}, status=status.HTTP_400_BAD_REQUEST)




@api_view(['POST'])
def logout_view(request):
    logout(request)  # This will clear the session
    return Response({"message": "Logout successful"}, status=status.HTTP_200_OK)


class UserProfileUpdateView(generics.UpdateAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = UserProfileSerializer

    def get_object(self):
        return self.request.user.profile

    def put(self, request, *args, **kwargs):
        serializer = self.get_serializer(self.get_object(), data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=HTTP_200_OK)
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)