from utils.RepeatedTimer import RepeatedTimer
from sampling.MagHandler import MagHandler
import threading
import time
mutex = threading.Lock()

timerOffset = 0.00
samplingPeriod = 1/10 - timerOffset


class MagSampling(threading.Thread):
    def __init__(self, bus):
        threading.Thread.__init__(self)
        self.mag = MagHandler(bus)
        self.sampleQueue = []
        self.running = False
        self.stop = False
        self.mutex = threading.Lock()
        self.startTime = 0
    
    def stopSampling(self):
        print("Stopping sampling")
        self.stop = True

    def getSample(self):        
        sample = self.mag.get_one_sample()
        if self.startTime == 0:
            self.startTime = time.perf_counter()
        sample[0] = (time.perf_counter() - self.startTime) * 1000
        self.saveSample(sample)
        return

    def saveSample(self, sample):
        mutex.acquire()
        self.sampleQueue.append(sample)
        mutex.release()
        return

    def getSampleQueue(self):
        mutex.acquire()
        tmp = self.sampleQueue.copy()
        self.sampleQueue.clear()
        mutex.release()
        return tmp

    def health(self):
        return self.mag.connect()

    def run(self):
        print("Starting sampling")
        if(self.running):
            print("Already running")
            return
        self.running = True
        if not self.mag.connect():
            print("Error connecting to Magnetometer")
            self.running = False
            return
        self.startTime = 0
        rt = RepeatedTimer(samplingPeriod, self.getSample)
        while(True):
            if self.stop:
                rt.stop()                
                time.sleep(0.1)
                print("Stopped sampling")
                break
            time.sleep(0.05)
        self.running = False

    def isRunning(self):
        return self.running
    