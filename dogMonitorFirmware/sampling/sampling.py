import smbus			#import SMBus module of I2C
from utils.RepeatedTimer import RepeatedTimer
from sampling.mpuSampling import MPUSampling
from sampling.magSampling import MagSampling
from utils.board import *
from services.helpers.Imu_helper import bulk_save_imu, bulk_save_magnetometer, bulk_save_temperature
import time
import threading

DEFAUL_DURATION_MS = 60*60*60 # 1 hour

class Sampling(threading.Thread):

    def __init__(self, id, duration):        
        threading.Thread.__init__(self)
        self.id = id
        self.stopFlag = False
        self.running = False
        self.duration = duration
        self.mpuSampling = MPUSampling(smbus.SMBus(3))
        self.tailMPUSampling = MPUSampling(smbus.SMBus(1))
        self.magSampling = MagSampling(smbus.SMBus(3))
        self.tailMagSampling = MagSampling(smbus.SMBus(1))
        if(duration == 0):
            self.duration = DEFAUL_DURATION_MS
        SetButton1Callback(self.stop_sampling)
        self.sensorHealth = {
            "imu1": False,
            "imu2": False,
            "tempature": False,
            "mic": False,
            "hr": False
        }
    
    def setSamplingParams(self, id, duration):
        self.id = id
        self.duration = duration
        return        

    def button1pressed():
        print("Button 1 pressed")
        return

    def button2pressed():
        print("Button 2 pressed")
        return

    def stop_sampling(self):
        self.stopFlag = True        
        print("Stopping sampling")
        return True

    def run(self):        
        # Prepare Flags
        print("Sampling started")
        self.stopFlag = False  
        self.running = True
        ledTimer = RepeatedTimer(0.5, ToogleGreenLed)
        
        # Prepare MPU sampling.
        self.mpuSampling.start()

        # Prepare tail MPU sampling.
        self.tailMPUSampling.start()

        # Prepare Mag sampling.
        self.magSampling.start()

        # Prepare tail Mag sampling.
        self.tailMagSampling.start()
        
        # Start Time.
        startTime = time.perf_counter()
        now = startTime
        lastSavedTime = startTime
        
        while(True):
            # Save data every 5 seconds.            
            now = time.perf_counter()          
            if lastSavedTime + 5 < now:
                lastSavedTime = now
                self.saveSamples()

            # Stop sampling if button 1 is pressed or if duration is reached.
            if self.stopFlag == True or (now - startTime) > self.duration:
                # Save last samples.
                self.saveSamples()

                # Stop MPU sampling.
                self.mpuSampling.stopSampling()
                time.sleep(0.5)
                if self.mpuSampling.isRunning():
                    print("Failed to Stop MPU sampling")

                # Stop tail MPU sampling.                
                self.tailMPUSampling.stopSampling()
                time.sleep(0.5)
                if self.tailMPUSampling.isRunning():
                    print("Failed to Stop MPU sampling")

                # Stop Mag sampling.
                self.magSampling.stopSampling()
                time.sleep(0.5)
                if self.magSampling.isRunning():
                    print("Failed to Stop Mag sampling")

                # Stop tail Mag sampling.
                self.tailMagSampling.stopSampling()
                time.sleep(0.5)
                if self.tailMagSampling.isRunning():
                    print("Failed to Stop Mag sampling")

                # Stop led timer.
                ledTimer.stop()
                GreenLedOn()
                break

            time.sleep(0.1)
        self.running = False
        self.stopFlag = False
        return

    def isRunning(self):
        return self.running

    def saveSamples(self):        
        # Save MPU1 samples
        mpu1Samples = self.mpuSampling.getSampleQueue()
        print("Samples mnpu1 saved: " + str(len(mpu1Samples)))        
        bulk_save_imu(self.id,mpu1Samples,"head")       
        # Save MPU2 samples
        mpu2Samples = self.tailMPUSampling.getSampleQueue()
        print("Samples mnpu2 saved: " + str(len(mpu2Samples)))        
        bulk_save_imu(self.id,mpu1Samples,"tail")      

        # Save Mag1 samples
        mag1Samples = self.magSampling.getSampleQueue()
        print("Samples mag1 saved: " + str(len(mag1Samples)))
        bulk_save_magnetometer(self.id,mag1Samples,"head")
        # Save Mag2 samples
        mag2Samples = self.tailMagSampling.getSampleQueue()
        print("Samples mag2 saved: " + str(len(mag2Samples)))
        bulk_save_magnetometer(self.id,mag2Samples,"tail")

        return
    
    def getHealth(self):
        status = {
            "temperature":False,
            "microphone":False,
            "imu_tail":self.mpuSampling.health(),
            "imu_head":self.tailMPUSampling.health(),
            "heart_rate":False
        }
        return status


samplingProcess = None

def startSampling(id, durationSeconds):
    global samplingProcess
    
    if samplingProcess == None:
        samplingProcess = Sampling(0, 10)

    if samplingProcess.isRunning():
        if samplingProcess.id != id:
            print("Another sampling is running")
            return False
        else:
            print("Sampling is already running")
            return True
    
    
    samplingProcess.setSamplingParams(id, durationSeconds)
    samplingProcess.start()
    time.sleep(1)
    if samplingProcess.isRunning():
        print("Sampling started Good")
        return True
    return False

def stopSampling():
    global samplingProcess
    
    if samplingProcess == None:
        print("No sampling is running")
        return True

    if not samplingProcess.isRunning():
        print("No sampling is running")
        return True
    
    # if samplingProcess.id != id:
    #     print("Another sampling is running")
    #     return True
    else:
        samplingProcess.stop_sampling()
        time.sleep(1)
        if samplingProcess.isRunning():
            print("Failed to Stop Sampling")
            return False
        return True
        
def isRunning():
    if samplingProcess == None:
        print("No sampling is running")
        return False

    if samplingProcess.isRunning():
        return True
    else: 
        return False

def getHealth():
    global samplingProcess
    
    if samplingProcess == None:
        samplingProcess = Sampling(0, 10)
    
    return samplingProcess.getHealth()
    