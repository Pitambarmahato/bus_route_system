from django.db import models
from root.utils import BaseModel

class Bus(BaseModel):
    bus_name = models.CharField(max_length=255)
    bus_number = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return f"{self.bus_name}"
