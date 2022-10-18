from django.db import models
from services.models import Routine
# Create your models here.
# Create your models here.
class Imu(models.Model):
    id = models.AutoField(primary_key=True)
    routine = models.ForeignKey(Routine,related_name="imu", on_delete=models.CASCADE)
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

class Magnetometer(models.Model):
    id = models.AutoField(primary_key=True)
    routine = models.ForeignKey(Routine,related_name="magnetometer", on_delete=models.CASCADE)
    sampled_at=models.IntegerField()
    m_x=models.FloatField()
    m_y=models.FloatField()
    m_z=models.FloatField()
    type=models.CharField(max_length=100)
    class Meta:
        db_table="magnetometer"
        
class Temperature(models.Model):
    id = models.AutoField(primary_key=True)
    routine = models.ForeignKey(Routine,related_name="temperature", on_delete=models.CASCADE)
    sampled_at=models.IntegerField()
    value = models.FloatField(default=0.0)
    class Meta:
        db_table="temperature"

class HeartRate(models.Model):
    id = models.AutoField(primary_key=True)
    routine = models.ForeignKey(Routine,related_name="heart_rate", on_delete=models.CASCADE)
    sampled_at=models.IntegerField()
    value = models.FloatField(default=0.0)
    class Meta:
        db_table="heart_rate"

class Audio(models.Model):
    id = models.AutoField(primary_key=True)
    routine = models.ForeignKey(Routine,related_name="audio", on_delete=models.CASCADE)
    file_name =models.CharField(max_length=300)
    class Meta:
        db_table="audio"