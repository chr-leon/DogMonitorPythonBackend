from pyexpat import model
from django.db import models

# Create your models here.
class Imu(models.Model):
    id = models.AutoField(primary_key=True)
    routineId = models.CharField(max_length=200)
    sampled_at=models.IntegerField()

    a_x=models.FloatField()
    a_y=models.FloatField()
    a_z=models.FloatField()

    g_x=models.FloatField()
    g_y=models.FloatField()
    g_z=models.FloatField()

    m_x=models.FloatField()
    m_y=models.FloatField()
    m_z=models.FloatField()

    type=models.CharField(max_length=100)

    class Meta:
        db_table="imu"
        