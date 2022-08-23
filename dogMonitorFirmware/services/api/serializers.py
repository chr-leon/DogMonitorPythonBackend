from rest_framework import serializers
import uuid

class RoutineSerializer(serializers.Serializer):
    type = serializers.CharField()
    routine_id = serializers.CharField()
    def validate(self, data):
        print("validating")
        if not ((data.get('type') == "stop_routine") or (data.get('type') == "stop_routine"))  :
             raise serializers.ValidationError("Los tipos de eventos deben ser start_routine ó stop_routine")
        try:
            uuid.UUID(str(data.get('routine_id')))
        except ValueError:
            raise serializers.ValidationError("El id de rutina debe ser un UUID")
        return data