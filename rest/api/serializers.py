from rest_framework import serializers
from .models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['email', 'username', 'password']
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def create(self, validate_data):
        return User.objects.create_user(**validate_data)


class VerifySerializer(serializers.Serializer):
    email = serializers.EmailField()
    otp = serializers.CharField()
