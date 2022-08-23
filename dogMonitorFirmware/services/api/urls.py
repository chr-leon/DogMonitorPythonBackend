from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from services.api.views import ServiceViewSet


app_name="services"

urlpatterns = [
    path('routine', ServiceViewSet.as_view({ 'post':'routine' })),
    path('status', ServiceViewSet.as_view({ 'get':'get_status' })),
]
 