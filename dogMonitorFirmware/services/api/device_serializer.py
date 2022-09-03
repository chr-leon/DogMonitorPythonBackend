from rest_framework import serializers
from services.models import Device

class ReadDeviceModelSerializer(serializers.ModelSerializer):
    class Meta:
        model=Device
        fields = ["id","name"]
        
class UpdateDeviceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Device
        fields = ['name']