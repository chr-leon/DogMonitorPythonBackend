import smbus			#import SMBus module of I2C
from utils.RepeatedTimer import RepeatedTimer
from sampling.mpuSampling import MPUSampling
from utils.board import *
from services.helpers.Imu_helper import bulk_save
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
        self.mpuSampling = None
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
        self.mpuSampling =  MPUSampling(smbus.SMBus(3))
        self.mpuSampling.start()
        
        # Start Time.
        startTime = time.time()
        now = startTime
        lastSavedTime = startTime
        
        while(True):
            # Save data every second.            
            now = time.time()            
            if lastSavedTime + 1 < now:
                lastSavedTime = now
                self.saveSamples()

            # Stop sampling if button 1 is pressed or if duration is reached.
            if self.stopFlag == True or (now - startTime) > self.duration:
                # Stop MPU sampling.
                self.saveSamples()
                self.mpuSampling.stopSampling()
                time.sleep(0.5)
                if self.mpuSampling.isRunning():
                    print("Failed to Stop MPU sampling")

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
        print("Saving samples")
        mpu1Samples = self.mpuSampling.getSampleQueue()
        print("MPU Samples: ")
        print(mpu1Samples)
        bulk_save(self.id,mpu1Samples,"head")
        print("----------------------------------------------------")
        return

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
    
    
    samplingProcess = Sampling(id,durationSeconds)
    samplingProcess.start()
    time.sleep(1)
    if samplingProcess.isRunning():
        print("Sampling started Good")
        return True
    return False

def stopSampling(id):
    global samplingProcess
    
    if samplingProcess == None:
        print("No sampling is running")
        return True

    if not samplingProcess.isRunning():
        print("No sampling is running")
        return True
    
    if samplingProcess.id != id:
        print("Another sampling is running")
        return True
    else:
        samplingProcess.stop_sampling()
        time.sleep(1)
        if samplingProcess.isRunning():
            print("Failed to Stop Sampling")
            return False
        return True
        