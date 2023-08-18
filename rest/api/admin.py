from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User


class CustomUserAdmin(UserAdmin):
    model = User
    list_display = ('id', 'password', 'last_login', 'is_superuser', 'username',
                    'last_name', 'is_staff', 'is_active', 'date_joined', 'email',
                    'about_me', 'is_verified', 'otp',)


admin.site.register(User, CustomUserAdmin)
