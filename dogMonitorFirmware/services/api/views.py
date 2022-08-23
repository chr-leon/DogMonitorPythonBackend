from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from services.api.serializers import RoutineSerializer

# Create your views here.
class ServiceViewSet(viewsets.ViewSet):
    def routine(self, request):
        generalPriceSerializer = RoutineSerializer(data=request.data)
        if not generalPriceSerializer.is_valid():
            return Response(generalPriceSerializer.errors,status=status.HTTP_400_BAD_REQUEST)
        print(request.data)
        print("here")
        return Response({},status=status.HTTP_200_OK)
    def get_status(self,request):
        simulatedStatus = {
            "running":False
        }
        return Response(simulatedStatus,status=status.HTTP_200_OK)
    def get_sensors_health(self,request):
        simulatedStatus = {
            "temperature":True,
            "microphone":True,
            "imu_tail":True,
            "imu_head":True,
            "heart_rate":True
        }
        return Response(simulatedStatus,status=status.HTTP_200_OK)
