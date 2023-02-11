from django.contrib import admin
from .models import Route, BusOperate


@admin.register(Route)
class RouteAdmin(admin.ModelAdmin):
    list_display = ('id', 'route_name', 'route_number')


@admin.register(BusOperate)
class BusOperateAdmin(admin.ModelAdmin):
    list_display = ('id', 'bus', 'route')
