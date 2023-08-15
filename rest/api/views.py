from django.shortcuts import render
from rest_framework import viewsets, permissions
from rest_framework.response import Response
from rest_framework.views import APIView
from .service import send_otp_via_email
from .models import User
from .serializers import UserSerializer, VerifySerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly
    ]
    serializer_class = UserSerializer


class VerifyOTP(APIView):
    def post(self, request):
        try:
            data = request.data
            serializer = VerifySerializer(data=data)
            if serializer.is_valid():
                email = serializer.data['email']
                otp = serializer.data['otp']

                user = User.objects.filter(email=email)
                if not user.exists():
                    return Response({
                        'status': '400',
                        'message': 'something went wrong',
                        'data': 'invalid name'
                    })

                if not user[0].otp == otp:
                    return Response({
                        'status': '400',
                        'message': 'something went wrong',
                        'data': 'wrong otp'
                    })

                user[0].is_verified = True
                user[0].save()

                return Response({
                    'status': '200',
                    'message': 'account verified',
                    'data': {}
                })

            return Response({
                'status': '400',
                'message': 'something went wrong',
                'data': serializer.errors
            })



        except Exception as e:
            print(e)
