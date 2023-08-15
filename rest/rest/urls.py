from django.contrib import admin
from django.urls import path, include
from api.views import VerifyOTP, RegisterAPI, custom500, custom404

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('api.urls')),
    path('register/', RegisterAPI.as_view()),
    path('verify/', VerifyOTP.as_view()),
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.jwt')),
]

handler404 = custom404
handler500 = custom500
