from django.http import JsonResponse
from rest_framework import permissions, generics, viewsets
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import User
from .serializers import UserSerializer, VerifySerializer
from .tasks import send_otp_email


class UserAPIView(viewsets.ModelViewSet):
    queryset = User.objects.all()
    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly
    ]
    serializer_class = UserSerializer


class RegisterAPI(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            send_otp_email.delay(serializer.data['email'])
            return Response({
                'status': '200',
                'message': 'you were successfully registrated, please check your email '
                           'to verify it',
            })
        return Response({
            'data': 'something went wrong(use another email)'
        })


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

                user = user.first()
                user.is_verified = True
                # dct = {'id': user.id, 'username': user.username, 'password': make_password(user.password),
                #        'email': user.email}
                # User.objects.delete(email=email)
                # User.objects.create(**dct)
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


def custom404(request, exception=None):
    return JsonResponse({
        'status_code': 404,
        'error': 'The resource was not found'
    })


def custom500(request):
    return JsonResponse({
        'status': '500',
        'message': 'Some problems on the server, please check this page later',
    }, status=500)
