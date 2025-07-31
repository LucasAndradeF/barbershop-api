from django.db import models
from barbers.models import Barber
from clients.models import Client
from services.models import Service
import uuid


class Appointment(models.Model):
    TYPE_CHOICES = (
        ("agendado", "Agendado"),
        ("concluido", "Concluído"),
        ("cancelado", "Cancelado"),
    )

    id = models.UUIDField(editable=False, primary_key=True, default=uuid.uuid4)
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    barber = models.ForeignKey(Barber, on_delete=models.CASCADE)
    service = models.ForeignKey(Service, on_delete=models.CASCADE)
    date = models.DateTimeField()
    status = models.CharField(
        max_length=10, choices=TYPE_CHOICES, default="agendado")
