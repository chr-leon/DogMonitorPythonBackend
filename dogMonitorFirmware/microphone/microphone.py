import pyaudio
import wave
import threading


form_1 = pyaudio.paInt16 # 16-bit resolution
chans = 1 # 1 channel
samp_rate = 44100 # 44.1kHz sampling rate
chunk = 4096 # 2^12 samples for buffer

class Microphone(threading.Thread):
    def __init__(self,routine_id):
        threading.Thread.__init__(self)
        self.routine_id =routine_id
        self.recording=False
        self.form_1 = pyaudio.paInt16 # 16-bit resolution
        self.chans = 1 # 1 channel
        self.samp_rate = 44100 # 44.1kHz sampling rate
        self.chunk = 4096 # 2^12 samples for buffer

        p = pyaudio.PyAudio()
        deviceName = "Microphone"
        self.deviceIndex = None
        for index in range(p.get_device_count()):
            fullDeviceName =p.get_device_info_by_index(index).get('name')
            if deviceName in fullDeviceName:
                self.deviceIndex = index
        
    def run(self):
        self.recording=True
        print(self.deviceIndex)
        audio = pyaudio.PyAudio() # create pyaudio instantiation
        stream = audio.open(format = form_1,rate = samp_rate,channels = chans, \
                        input_device_index = self.deviceIndex,input = True, \
                        frames_per_buffer=chunk)
        frames = []
        while(True):
            if not self.recording:
                break
            print("Recording--------------->")
            data = stream.read(chunk)
            frames.append(data)
        print("recordong finished")
        stream.stop_stream()
        stream.close()
        audio.terminate()
        wavefile = wave.open(self.routine_id+".wav",'wb')
        wavefile.setnchannels(chans)
        wavefile.setsampwidth(audio.get_sample_size(form_1))
        wavefile.setframerate(samp_rate)
        wavefile.writeframes(b''.join(frames))
        wavefile.close()

    def stop(self):
        self.recording=False
        print("stoped")
    def isRecording(self):
        return self.recording


recordProcess = None

def startRecording(routineId):
    global recordProcess
    #if recordProcess == None:
    recordProcess = Microphone(routineId)    
    recordProcess.start()
    return False
def stopRecording():
    if  not recordProcess == None:
        recordProcess.stop()
