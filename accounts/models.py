from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission, UserManager
import uuid


class User(AbstractUser):
    USER_TYPE_CHOICES = [
        ('client', 'Cliente'),
        ('barber', 'Barbeiro'),
    ]

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    phone = models.CharField(max_length=20)
    email = models.EmailField(max_length=255, unique=True)

    user_type = models.CharField(max_length=20, choices=USER_TYPE_CHOICES)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'first_name', 'last_name']

    objects = UserManager()

    groups = models.ManyToManyField(Group)

    user_permissions = models.ManyToManyField(Permission)

    def __str__(self):
        return f'{self.first_name} ({self.user_type})'
