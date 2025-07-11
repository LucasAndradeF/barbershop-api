from django.db import models
from django.contrib.auth.models import AbstractUser
import uuid


class Barber(AbstractUser):
    CHOICES_TYPE_ESPECIALIDADE = (
        ('corte', 'Corte'),
        ('barba', 'Barba'),
        ('sobrancelha', 'Sobrancelha'),
        ('platinado', 'Platinado'),
        ('hidratacao', 'Tratamento Capilar'),
    )

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    especialidade = models.CharField(
        choices=CHOICES_TYPE_ESPECIALIDADE, max_length=50, null=False, blank=False)
    phone = models.CharField(max_length=20)
    email = models.EmailField(max_length=255, unique=True)

    def __str__(self):
        return self.first_name

    class Meta:
        verbose_name = 'Barbeiro'
        verbose_name_plural = 'Barbeiros'
