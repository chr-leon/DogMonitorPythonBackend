from services.models import Routine
from sensors.models import Imu, Magnetometer, Temperature,HeartRate,Audio

### Imu indexe
TIME_INDEX=0
AX_INDEX=1
AY_INDEX=2
AZ_INDEX=3
GX_INDEX=4
GY_INDEX=5
GZ_INDEX=6
MX_INDEX=1
MY_INDEX=2
MZ_INDEX=3

### temperature index
TEMPERATURE_INDEX=1
##heart rate index
HEART_RATE_INDEX=1


def bulk_save_imu(routineId,data,sensorType):
    routineQuerySet = Routine.objects.all()
    routine = routineQuerySet.get(pk=routineId)
    listOfRecords = []
    for record in data:
        imu = Imu(
             sampled_at=record[TIME_INDEX],
             a_x=record[AX_INDEX],
            a_y=record[AY_INDEX],
            a_z=record[AZ_INDEX],
            g_x=record[GX_INDEX],
            g_y=record[GY_INDEX],
            g_z=record[GZ_INDEX],
            type=sensorType,
            routine=routine
        )
        listOfRecords.append(imu)
    Imu.objects.bulk_create(listOfRecords)
    # print(listOfRecords)

def bulk_save_magnetometer(routineId,data,sensorType):
    routineQuerySet = Routine.objects.all()
    routine = routineQuerySet.get(pk=routineId)
    listOfRecords = []
    for record in data:
        imu = Magnetometer(
            sampled_at=record[TIME_INDEX],
            m_x=record[MX_INDEX],
            m_y=record[MY_INDEX],
            m_z=record[MZ_INDEX],
            type=sensorType,
            routine=routine
        )
        listOfRecords.append(imu)
    Magnetometer.objects.bulk_create(listOfRecords)
    # print(listOfRecords)

def bulk_save_temperature(routineId,data):
    routineQuerySet = Routine.objects.all()
    routine = routineQuerySet.get(pk=routineId)
    listOfRecords = []
    for record in data:
        temperature = Temperature(
             sampled_at=record[TIME_INDEX],
             value=record[TEMPERATURE_INDEX],
            routine=routine
        )
        listOfRecords.append(temperature)
    Temperature.objects.bulk_create(listOfRecords)
    print(listOfRecords)

def bulk_save_heart_rate(routineId,data):
    routineQuerySet = Routine.objects.all()
    routine = routineQuerySet.get(pk=routineId)
    listOfRecords = []
    for record in data:
        heart_rate = HeartRate(
             sampled_at=record[TIME_INDEX],
             value=record[HEART_RATE_INDEX],
            routine=routine
        )
        listOfRecords.append(heart_rate)
    HeartRate.objects.bulk_create(listOfRecords)
    print(listOfRecords)

def save_file_name(routineId,fileName):
    routineQuerySet = Routine.objects.all()
    routine = routineQuerySet.get(pk=routineId)
    audio = Audio(
        file_name=fileName,
        routine=routine
    )
    audio.save()