from django.urls import path
from .views import BusView, BusRouteView, IndexPageView


urlpatterns = [
    path("", IndexPageView.as_view(), name="index"),
    path('buses/', BusView.as_view(), name="bus"),
    path('buses/<int:pk>/route/', BusRouteView.as_view(), name="bus_detail"),
]
