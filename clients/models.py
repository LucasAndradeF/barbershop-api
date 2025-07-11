from django.db import models
from core.models import User


class Client(User):
    user_type = models.CharField(max_length=20, default='client')

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

    class Meta:
        verbose_name = 'Cliente'
        verbose_name_plural = 'Clientes'
