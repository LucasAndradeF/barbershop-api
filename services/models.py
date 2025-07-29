from django.db import models
import uuid

class Service(models.Model):
    id = models.UUIDField(editable=False, primary_key=True, default=uuid.uuid4)
    name = models.CharField(max_length=255)
    duration = models.TimeField()
    price = models.DecimalField(max_digits=7, decimal_places=2)

