from django.db import models
from accounts.models import User


class Barber(models.Model):
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, related_name='barber_profile')

    CHOICES_TYPE_ESPECIALIDADE = (
        ('corte', 'Corte'),
        ('barba', 'Barba'),
        ('sobrancelha', 'Sobrancelha'),
        ('platinado', 'Platinado'),
        ('hidratacao', 'Tratamento Capilar'),
    )

    especialidade = models.CharField(
        choices=CHOICES_TYPE_ESPECIALIDADE, max_length=50, null=False, blank=False)

    def __str__(self):
        return f'{self.user.first_name} {self.user.last_name}'

    class Meta:
        verbose_name = 'Barbeiro'
        verbose_name_plural = 'Barbeiros'
