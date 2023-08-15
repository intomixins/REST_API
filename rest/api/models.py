from django.db import models
from django.contrib.auth.models import AbstractUser
from .managers import UserManager


class User(AbstractUser):
    email = models.EmailField(unique=True)
    about_me = models.TextField(max_length=1000)
    is_verified = models.BooleanField(default=False)
    otp = models.CharField(max_length=6, null=True, blank=True)

    # USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['email', 'about_me']

    objects = UserManager()
