from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from services.api.serializers import RoutineSerializer
from services.models import Imu
from services.helpers import Imu_helper

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
        #routineId = 1
        #sensorType = "tail"
        #data = [[100,1.001,2.123,3,4,5,6,7,8,9],[200,4,5,6,7,8,9,10,11,12],[300,7,8,9,10,11,12,13,14,15]]
        #Imu_helper.bulk_save(routineId,data,sensorType)
        simulatedStatus = {
            "temperature":True,
            "microphone":True,
            "imu_tail":True,
            "imu_head":True,
            "heart_rate":True
        }
        return Response(simulatedStatus,status=status.HTTP_200_OK)
