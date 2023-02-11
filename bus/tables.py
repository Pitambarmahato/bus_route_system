from django_tables2 import SingleTableView, tables
from django.utils.safestring import mark_safe
import itertools
from .models import Bus
from routes.models import BusOperate


class BusTable(tables.Table):
    route_count = tables.columns.Column(empty_values=())

    class Meta:
        model = Bus
        sequence = ('bus_name', 'bus_number', 'route_count')
        exclude = ('created_at', 'updated_at', 'is_active', 'is_deleted', 'id')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.counter = itertools.count()


    def render_route_count(self, value, record):
        bus = Bus.objects.get(bus_number = record.get('bus_number'))
        return mark_safe("<a href= %s><b>%s</b></a>" % ("/buses/"+str(bus.id)+"/route/", bus.bus.count()))

    def order_route_count(self, queryset, is_descending):
        queryset = queryset.order_by("-id" if is_descending else "id")
        return (queryset, True)


class BusRouteTable(tables.Table):
    route_name = tables.columns.Column(empty_values=())
    route_number = tables.columns.Column(empty_values=())

    class Meta:
        model = BusOperate
        sequence = ('route_name', 'route_number', 'from_time', 'to_time')
        exclude = ('id', 'is_active', 'created_at', 'updated_at', 'route', 'bus', 'is_deleted')

    def render_route_name(self, value, record):
        return mark_safe(record.route.route_name)

    def order_route_name(self, queryset, is_descending):
        queryset = queryset.order_by("-route_id" if is_descending else "route_id")
        return (queryset, True)

    def render_route_number(self, value, record):
        return mark_safe(record.route.route_number)

    def order_route_number(self, queryset, is_descending):
        queryset = queryset.order_by("-route_id" if is_descending else "route_id")
        return (queryset, True)