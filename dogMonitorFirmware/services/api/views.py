from sre_constants import SUCCESS
from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from services.api.device_serializer import ReadDeviceModelSerializer, UpdateDeviceSerializer
from services.api.routine_serializers import ReadRoutineByIdSerializer, ReadRoutineModelSerializer, CreateRoutineSerializer
from rest_framework.generics import ListAPIView 
from django.db.models import Q
from sampling.sampling import startSampling, isRunning, getHealth
from sampling.sampling import stopSampling
from services.helpers.Imu_helper import bulk_save_heart_rate, bulk_save_imu, bulk_save_magnetometer, bulk_save_temperature, save_file_name
from services.models import Routine,Device
from rest_framework.filters import SearchFilter, OrderingFilter



# Create your views here.
class ServiceViewSet(viewsets.ViewSet):
    # def routine(self, request):
    #     serializer = RoutineSerializer(data=request.data)
    #     if not serializer.is_valid():
    #         return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    #     print(request.data)
        
    #     # Extract data from request.
    #     routineId = request.data['routine_id']
    #     type = request.data['type']

    #     # Start sampling.
    #     succes = False
    #     if type == "start_routine":
    #         duration = request.data['duration']
    #         succes = startSampling(routineId,duration)
    #         print("Routine Started: " + str(succes))
    #     elif type == "stop_routine":
    #         print("Routine Stopped")
    #         succes = stopSampling(routineId)        
        
    #     if succes:
    #         return Response(status=status.HTTP_200_OK)
    #     else:
    #         return Response(status=status.HTTP_400_BAD_REQUEST)
        
    def get_status(self,request):
        simulatedStatus = {
            "running":False
        }
        return Response(simulatedStatus,status=status.HTTP_200_OK)
    def get_sensors_health(self,request):
        #routineId = 1
        #sensorType = "tail"
        #data = [[100,1.001,2.123,3,4,5,6,7,8,9],[200,4,5,6,7,8,9,10,11,12],[300,7,8,9,10,11,12,13,14,15]]
        #Imu_helper.bulk_save_imu(routineId,data,sensorType)
        simulatedStatus = {
            "temperature":True,
            "microphone":True,
            "imu_tail":True,
            "imu_head":True,
            "heart_rate":True
        }
        return Response(getHealth(),status=status.HTTP_200_OK)


class DeviceViewSet(viewsets.ViewSet):
    def get_device(self,request):
        querySet = Device.objects.all()
        devices = querySet.filter(pk=1)
        serializer = ReadDeviceModelSerializer(devices[0])
        return Response(serializer.data,status=status.HTTP_200_OK)
    def update_device(self,request):
        querySet = Device.objects.all()
        devices = querySet.filter(pk=1)
        serializer = UpdateDeviceSerializer(
                instance=devices[0],
                data=request.data
        )
        if serializer.is_valid(): 
            serializer.save()
        return Response(serializer.data,status=status.HTTP_200_OK)


class RoutineViewSet(viewsets.ViewSet):
    def search_routine(self,request):
        querySet = Routine.objects.all()
        searchString = request.GET.get('search',None)
        if searchString == None:
            print("no filter")
            serializer = ReadRoutineModelSerializer(querySet,many=True)
            return Response(serializer.data,status=status.HTTP_200_OK)
        else:
            print("using filter: ",searchString)
            filteredRoutines = querySet.filter(Q(dog_name__startswith=searchString))
            serializer = ReadRoutineModelSerializer(filteredRoutines,many=True)
            return Response(serializer.data,status=status.HTTP_200_OK)
    def create_and_start_routine(self,request):                
        serializer = CreateRoutineSerializer(data=request.data)        
        if not serializer.is_valid():
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
        isAlreadyRunning =isRunning()
        if(isAlreadyRunning):
            return Response({"message":"Existe una rutina en curso"},status=400)
        serializer.save()        
        routineId=serializer.data['id']        
        ######################## save data simulation
        # dataImu = [
        #     [0,1,2,3,4,5,6,7,8,9],
        #     [0,1,2,3,4,5,6,7,8,9],
        #     [0,1,2,3,4,5,6,7,8,9]
        # ]
        # bulk_save_imu(routineId=routineId,data=dataImu,sensorType="tail")

        # dataTemperature = [
        #     [0,1],
        #     [3,4],
        #     [5,6]
        # ]
        # bulk_save_temperature(routineId=routineId,data=dataTemperature)

        # dataHeartRate = [
        #     [0,1],
        #     [3,4],
        #     [5,6]
        # ]
        # bulk_save_heart_rate(routineId=routineId,data=dataHeartRate)
        dataMagnetometer = [
            [2,0,1,2],
            [2,3,4,5],
            [2,6,7,8]
        ]
        bulk_save_magnetometer(routineId=routineId,data=dataMagnetometer,sensorType="tail")

        # save_file_name(routineId=routineId,fileName=serializer.data['name']+".mp3")
        ###########################
        succes = startSampling(serializer.data['id'],300)        
        return Response({"success":succes,"data":serializer.data},status=status.HTTP_200_OK)

    def delete_routine(self,request,pk=None):
        queryset = Routine.objects.all()
        routine = queryset.get(pk=pk)
        routine.delete()
        return Response(status=200)
    def stop_routine(self,request):
        succes = stopSampling()
        return Response({"success":succes},status=status.HTTP_200_OK)
        
    def get_routine_by_id(self,request,pk):
        queryset = Routine.objects.all()
        routine = queryset.get(pk=pk)
        serializer = ReadRoutineByIdSerializer(routine)
        return Response(serializer.data,status=200)


