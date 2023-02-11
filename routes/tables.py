from django_tables2 import SingleTableView, tables
from django.utils.safestring import mark_safe
import itertools
from .models import Route, BusOperate
from bus.models import Bus


class RouteTable(tables.Table):
    bus_count = tables.columns.Column(empty_values=())

    class Meta:
        model = Route
        template_name = "django_tables2/bootstrap5.html"
        sequence = ('route_name', 'route_number', 'bus_count')
        exclude = ('created_at', 'updated_at', 'is_active', 'is_deleted', 'id')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.counter = itertools.count()


    def render_bus_count(self, value, record):
        route = Route.objects.get(route_number = record.get('route_number'))
        return mark_safe("<a href= %s><b>%s</b></a>" % ("/route/"+str(route.id)+"/", route.route.count()))


class RouteDetailsTable(tables.Table):
    bus_name = tables.columns.Column(empty_values=())
    bus_number = tables.columns.Column(empty_values=())

    class Meta:
        model = BusOperate
        sequence = ('bus_name', 'bus_number', 'from_time', 'to_time')
        exclude = ('id', 'is_active', 'created_at', 'is_deleted', 'bus', 'route', 'updated_at')

    def render_bus_name(self, value, record):
        return record.bus.bus_name

    def render_bus_number(self, value, record):
        return record.bus.bus_number