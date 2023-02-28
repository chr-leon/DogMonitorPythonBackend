import pyaudio
import wave

form_1 = pyaudio.paInt16 # 16-bit resolution
chans = 1 # 1 channel
samp_rate = 44100 # 44.1kHz sampling rate
chunk = 4096 # 2^12 samples for buffer

def getDeviceIndex():
    p = pyaudio.PyAudio()
    deviceName = "Microphone"
    deviceIndex = None
    for index in range(p.get_device_count()):
        fullDeviceName =p.get_device_info_by_index(index).get('name')
        if deviceName in fullDeviceName:
            deviceIndex = index
    return deviceIndex

# def recordAudio(time_in_seconds,usb_device_index,file_name):
#     audio = pyaudio.PyAudio() # create pyaudio instantiation
#     stream = audio.open(format = form_1,rate = samp_rate,channels = chans, \
#                         input_device_index = usb_device_index,input = True, \
#                         frames_per_buffer=chunk)
#     print("recording")
#     frames = []

#     # loop through stream and append audio chunks to frame array
#     for ii in range(0,int((samp_rate/chunk)*time_in_seconds)):
#         data = stream.read(chunk)
#         frames.append(data)

#     print("finished recording")

#     # stop the stream, close it, and terminate the pyaudio instantiation
#     stream.stop_stream()
#     stream.close()
#     audio.terminate()

#     # save the audio frames as .wav file
#     wavefile = wave.open(file_name,'wb')
#     wavefile.setnchannels(chans)
#     wavefile.setsampwidth(audio.get_sample_size(form_1))
#     wavefile.setframerate(samp_rate)
#     wavefile.writeframes(b''.join(frames))
#     wavefile.close()
        


deviceIndex= getDeviceIndex();
print(deviceIndex)
#recordAudio(6,deviceIndex,"test1.wav")
counter=0
audio = pyaudio.PyAudio() # create pyaudio instantiation
stream = audio.open(format = form_1,rate = samp_rate,channels = chans, \
                        input_device_index = deviceIndex,input = True, \
                        frames_per_buffer=chunk)
print("recording")
frames = []
while(counter<50):
    print("recording:",counter)
    counter = counter+1
    data = stream.read(chunk)
    frames.append(data)

print("recordong finished")
stream.stop_stream()
stream.close()
audio.terminate()
wavefile = wave.open("test2.wav",'wb')
wavefile.setnchannels(chans)
wavefile.setsampwidth(audio.get_sample_size(form_1))
wavefile.setframerate(samp_rate)
wavefile.writeframes(b''.join(frames))
wavefile.close()



