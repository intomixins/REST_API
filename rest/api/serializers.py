from rest_framework import serializers
from .models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'about_me', 'is_verified', )


class VerifySerializer(serializers.Serializer):
    email = serializers.EmailField()
    otp = serializers.CharField()
