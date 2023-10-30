from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    username = None,
    email = models.EmailField(unique=True, verbose_name="почта")

    is_active = models.BooleanField(verbose_name='активный пользователь', default=False)
    verify_code = models.CharField(max_length=50, verbose_name='Верификация')
    is_manager = models.BooleanField(default=False)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []
