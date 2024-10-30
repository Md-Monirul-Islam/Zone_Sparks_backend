from rest_framework import serializers
from .models import Account, UserProfile

class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = ['id', 'email', 'is_active', 'is_staff']



class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ['full_name', 'phone', 'profile_image']

    def update(self, instance, validated_data):
        # Update the instance with the validated data
        instance.full_name = validated_data.get('full_name', instance.full_name)
        instance.phone = validated_data.get('phone', instance.phone)
        profile_image = validated_data.get('profile_image', None)
        if profile_image:
            instance.profile_image = profile_image
        instance.save()
        return instance
