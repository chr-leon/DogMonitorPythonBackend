from microphone import startRecording,stopRecording

startRecording("1")
for i in range(0,5000):
    print(i)
stopRecording()
    