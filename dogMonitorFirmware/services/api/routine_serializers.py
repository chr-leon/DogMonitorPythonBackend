import os
from rest_framework import serializers
from services.api.sensors_serializer import ReadAudioModelSerializer, ReadHeartRateModelSerializer, ReadImuModelSerializer, ReadMagnetometerModelSerializer, ReadTemperatureModelSerializer
from services.models import Routine
import os
from django.conf import settings
import base64

class CreateRoutineSerializer(serializers.ModelSerializer):
    ##routine_id = serializers.CharField()
    # def validate(self, data):
    #     print("validating")
    #     if not ((data.get('type') == "start_routine") or (data.get('type') == "stop_routine"))  :
    #          raise serializers.ValidationError("Los tipos de eventos deben ser start_routine ó stop_routine")
    #     try:
    #         if int(data.get('routine_id')) <= 0:
    #             raise serializers.ValidationError("El id de la rutina debe ser mayor a 0")
    #     except ValueError:
    #         raise serializers.ValidationError("El id de rutina debe ser un numero")
    #     return data
    class Meta:
        model=Routine
        fields = ["id","name","dog_name"]

class ReadRoutineModelSerializer(serializers.ModelSerializer):
    class Meta:
        model=Routine
        fields = ["id","name","dog_name"]

class ReadRoutineByIdSerializer(serializers.ModelSerializer):
    imu = ReadImuModelSerializer(many=True)
    temperature =ReadTemperatureModelSerializer(many=True)
    heart_rate = ReadHeartRateModelSerializer(many=True)
    audio = ReadAudioModelSerializer(many=True)
    magnetometer = ReadMagnetometerModelSerializer(many=True)
    class Meta:
        model=Routine
        fields = ["id","name","dog_name",'imu','heart_rate','audio','temperature','magnetometer']
    def to_representation(self, instance):
        representation = super().to_representation(instance)
        filePath =os.path.join(settings.BASE_DIR)+"/dogMonitorFirmware/audio/"
        #print(filePath)
        fileName=representation['audio'][0]['file_name'];
        file_ = open(filePath+fileName,mode='rb')
        encoded_string = base64.b64encode(file_.read())
        #print(encoded_string)
        representation['audio'][0]["data"] = encoded_string

        return representation