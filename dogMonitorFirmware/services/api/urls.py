from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from services.api.views import ServiceViewSet,DeviceViewSet


app_name="services"

urlpatterns = [

    path('device', DeviceViewSet.as_view({ 'get':'get_device' })),
    path('routine', ServiceViewSet.as_view({ 'post':'routine' })),
    path('status', ServiceViewSet.as_view({ 'get':'get_status' })),
    path('health', ServiceViewSet.as_view({ 'get':'get_sensors_health' })),
]
 