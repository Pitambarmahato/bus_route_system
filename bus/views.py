from django.views.generic import TemplateView, DetailView
from django_tables2 import SingleTableView
from .models import Bus
from routes.models import BusOperate
from .tables import BusTable, BusRouteTable


class IndexPageView(TemplateView):
    template_name = "index.html"


class BusView(SingleTableView):
    table_class = BusTable
    template_name = 'bus.html'
    queryset = Bus.objects.values('bus_name', 'bus_number')

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        print(self.get_table_data())
        return context


class BusRouteView(SingleTableView):
    template_name = "bus_route.html"
    table_class = BusRouteTable

    def get_queryset(self):
        return BusOperate.objects.filter(bus__id=self.kwargs['pk'])

