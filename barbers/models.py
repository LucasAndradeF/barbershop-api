from django.db import models
from core.models import User


class Barber(User):
    CHOICES_TYPE_ESPECIALIDADE = (
        ('corte', 'Corte'),
        ('barba', 'Barba'),
        ('sobrancelha', 'Sobrancelha'),
        ('platinado', 'Platinado'),
        ('hidratacao', 'Tratamento Capilar'),
    )

    especialidade = models.CharField(
        choices=CHOICES_TYPE_ESPECIALIDADE, max_length=50, null=False, blank=False)
    user_type = models.CharField(max_length=20, default='barber')

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

    class Meta:
        verbose_name = 'Barbeiro'
        verbose_name_plural = 'Barbeiros'
