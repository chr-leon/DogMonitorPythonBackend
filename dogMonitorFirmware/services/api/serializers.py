from rest_framework import serializers
import uuid

class RoutineSerializer(serializers.Serializer):
    type = serializers.CharField()
    routine_id = serializers.CharField()
    def validate(self, data):
        print("validating")
        if not ((data.get('type') == "start_routine") or (data.get('type') == "stop_routine"))  :
             raise serializers.ValidationError("Los tipos de eventos deben ser start_routine ó stop_routine")
        try:
            if int(data.get('routine_id')) <= 0:
                raise serializers.ValidationError("El id de la rutina debe ser mayor a 0")
        except ValueError:
            raise serializers.ValidationError("El id de rutina debe ser un numero")
        return data