from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from services.api.views import RoutineListView, ServiceViewSet,DeviceViewSet


app_name="services"

urlpatterns = [

    #Device services
    path('device', DeviceViewSet.as_view({ 'get':'get_device' })),
    path('device/1', DeviceViewSet.as_view({ 'put':'update_device' })),
    
    #RoutineServices
    path('routine/list', ServiceViewSet.as_view({ 'post':'routine' })),
    path('routine', RoutineListView.as_view() , name = "list_routines"),

    path('status', ServiceViewSet.as_view({ 'get':'get_status' })),
    path('health', ServiceViewSet.as_view({ 'get':'get_sensors_health' })),
]
 