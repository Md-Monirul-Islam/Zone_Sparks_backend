from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from rest_framework.views import APIView
from django.contrib.auth import get_user_model
from rest_framework import generics, permissions
from account_app.models import Account,UserProfile
from account_app.serializers import UserProfileSerializer


# Create your views here.
User = get_user_model()

class UserProfileView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, user_id):
        profile = get_object_or_404(UserProfile, user__id=user_id)
        data = {
            "full_name": profile.full_name,
            "phone": profile.phone,
            "email": profile.user.email,
            "profile_image": profile.profile_image.url if profile.profile_image else None,
        }
        return JsonResponse(data)

class UpdateUserProfileView(generics.RetrieveUpdateAPIView):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        # Return the user's profile
        return self.request.user.userprofile