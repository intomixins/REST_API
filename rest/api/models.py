from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    email = models.EmailField(unique=True)
    about_me = models.TextField(max_length=1000)

    REQUIRED_FIELDS = ['email', ]
