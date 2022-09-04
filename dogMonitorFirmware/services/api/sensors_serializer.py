# from rest_framework import serializers
# from sensors.models import Audio, HeartRate, Imu, Temperature

# class ReadImuModelSerializer(serializers.ModelSerializer):
#     class Meta:
#         model=Imu
#         fields = [
#             "id",
#             "sampled_at",
#             "a_x",
#             "a_y",
#             "a_z",
#             "g_x",
#             "g_y",
#             "g_z",
#             "m_x",
#             "m_y",
#             "m_z",
#             "type"
#         ]

# class ReadTemperatureModelSerializer(serializers.ModelSerializer):
#     class Meta:
#         model=Temperature
#         fields = ["id","sampled_at","value"]

# class ReadHeartRateModelSerializer(serializers.ModelSerializer):
#     class Meta:
#         model=HeartRate
#         fields = ["id","sampled_at","value"]

# class ReadAudioModelSerializer(serializers.ModelSerializer):
#     class Meta:
#         model=Audio
#         fields = ["id","file_name"]