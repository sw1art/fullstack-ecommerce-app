from rest_framework import serializers
from .models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            'user_id', 'username', 'email', 'phone_number', 'avatar_url', 'address',
            'is_verified', 'created_at'
        ]