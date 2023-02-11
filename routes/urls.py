from django.urls import path
from .views import RouteView, RouteDetailView


urlpatterns = [
    path("route/", RouteView.as_view(), name="routes"),
    path("route/<int:pk>/", RouteDetailView.as_view(), name="route_detail"),
]