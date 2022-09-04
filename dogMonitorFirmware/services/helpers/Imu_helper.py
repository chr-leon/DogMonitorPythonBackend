from services.models import Imu

TIME_INDEX=0
AX_INDEX=1
AY_INDEX=2
AZ_INDEX=3
GX_INDEX=4
GY_INDEX=5
GZ_INDEX=6
MX_INDEX=7
MY_INDEX=8
MZ_INDEX=9


def bulk_save(routineId,data,sensorType):
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
            m_x=record[MX_INDEX],
            m_y=record[MY_INDEX],
            m_z=record[MZ_INDEX],
            type=sensorType,
            routine=routineId
        )
        listOfRecords.append(imu)
    Imu.objects.bulk_create(listOfRecords)
    print(listOfRecords)