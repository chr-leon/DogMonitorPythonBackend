from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from services.api.views import ServiceViewSet,DeviceViewSet,RoutineViewSet


app_name="services"

urlpatterns = [

    #Device services
    path('device', DeviceViewSet.as_view({ 'get':'get_device' })),
    path('device/1', DeviceViewSet.as_view({ 'put':'update_device' })),
    
    #RoutineServices
    path('routine', RoutineViewSet.as_view({ 'post':'create_and_start_routine' })),
    path('routine/list', RoutineViewSet.as_view({ 'get':'search_routine' })),

    path('status', ServiceViewSet.as_view({ 'get':'get_status' })),
    path('health', ServiceViewSet.as_view({ 'get':'get_sensors_health' })),
]
 