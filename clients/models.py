from django.db import models
from django.contrib.auth.models import AbstractUser
import uuid


class Client(AbstractUser):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    phone = models.CharField(max_length=20)
    email = models.EmailField(max_length=255, unique=True)

    USERNAME_FIELD = email
    REQUIRED_FIELDS = ['first_name', 'last_name']

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

    class Meta:
        verbose_name = 'Cliente'
        verbose_name_plural = 'Clientes'
 