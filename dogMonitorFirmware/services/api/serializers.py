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
        # if len(data.get('new_password')) < 8:
        #     raise serializers.ValidationError("Las nuevas contraseñas deben ser de al menos 9 caracteres")
        # validCurrentPassword=check_password(data.get('current_password'),self.context.get("encrypted_password"))
        # if not validCurrentPassword:
        #     raise serializers.ValidationError("Contraseña actual incorrecta")
        return data