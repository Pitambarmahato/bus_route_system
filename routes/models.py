from django.db import models
from django.db.models import Q
from django.core.exceptions import ValidationError
from root.utils import BaseModel
from bus.models import Bus

class Route(BaseModel):
    route_name = models.CharField(max_length=255)
    route_number = models.IntegerField(unique=True)

    def __str__(self):
        return f"{self.route_name}"


class BusOperate(BaseModel):
    route = models.ForeignKey(Route, related_name="route", on_delete=models.DO_NOTHING)
    bus = models.ForeignKey(Bus, related_name="bus", on_delete=models.DO_NOTHING)
    from_time = models.DateTimeField()
    to_time = models.DateTimeField()

    def __str__(self):
        return f"{self.route.route_name}"

    def clean(self):
        if self.from_time > self.to_time:
            raise ValidationError("From Time Should be less than to time.")
        if __class__.objects.filter(Q(bus_id=self.bus.id, from_time__lte=self.from_time, to_time__gte=self.from_time) or Q(bus_id=self.bus.id, from_time__lte=self.to_time, to_time__gte=self.to_time)).exists():
            raise ValidationError("This Bus already operating in another route.")
        if __class__.objects.filter(Q(bus_id=self.bus.id, from_time__range=(self.from_time, self.to_time)) or Q(bus_id=self.bus.id, to_time__range=(self.from_time, self.to_time))).exists():
            raise ValidationError("Bus already operating in another route.")
        return self.bus