from django.views.generic import TemplateView
from django_tables2 import SingleTableView
from .models import Route, BusOperate
from .tables import RouteTable, RouteDetailsTable


class RouteView(SingleTableView):
    table_class = RouteTable
    template_name = 'route.html'
    queryset = Route.objects.values('route_name', 'route_number')

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['bus_count'] = 5
        print(self.get_table_data())
        return context


class RouteDetailView(SingleTableView):
    table_class = RouteDetailsTable
    template_name = 'route_detail.html'

    def get_queryset(self):
        return BusOperate.objects.filter(route__id=self.kwargs['pk'])