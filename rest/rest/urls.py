from django.contrib import admin
from django.urls import path, include
from api.views import VerifyOTP

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('api.urls')),
    path('verify/', VerifyOTP.as_view()),
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.jwt')),
]
