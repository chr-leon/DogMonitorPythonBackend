from rest_framework import serializers
#from services.api.sensors_serializer import ReadAudioModelSerializer, ReadHeartRateModelSerializer, ReadImuModelSerializer, ReadTemperatureModelSerializer
from services.models import Routine

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
    #imus = ReadImuModelSerializer(many=True)
    #temperatures =ReadTemperatureModelSerializer(many=True)
    # heart_rate = ReadHeartRateModelSerializer(many=True)
    # audio = ReadAudioModelSerializer(many=True)
    class Meta:
        model=Routine
        fields = ["id","name","dog_name"] #,'heart_rate','audio','imu']