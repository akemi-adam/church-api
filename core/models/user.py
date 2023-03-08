from django.utils import timezone
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from core.managers import UserManager

class User(AbstractBaseUser, PermissionsMixin):
    
    username = models.CharField(max_length = 80, verbose_name = 'Username')

    password = models.CharField(max_length = 300, verbose_name = 'Password')

    email = models.EmailField(max_length = 255, unique = True, verbose_name = 'E-mail')

    is_staff = models.BooleanField(default = False, verbose_name = 'Staff')

    is_superuser = models.BooleanField(default = False, verbose_name = 'Super User')

    date_joined = models.DateTimeField(default = timezone.now)

    user_wing = models.ForeignKey('core.Wing', on_delete = models.CASCADE, verbose_name = 'Wing', related_name = 'wing_user_set', default = 1)

    wings = models.ManyToManyField('core.Wing', through = 'Due')

    objects = UserManager()

    USERNAME_FIELD = 'email'

    REQUIRED_FIELDS = []

    def __str__(self) -> str:
        return f'{self.username}: {self.email}'