from gpiozero import LED
from gpiozero import Button

greenLed = LED(16)
redLed = LED(20)

button1 = Button(19)
button2 = Button(26)

def GreenLedOn():
    greenLed.on()

def ToogleGreenLed():
    greenLed.toggle()

def ToogleRedLed():
    redLed.toggle()

def GreenLedOff():
    greenLed.off()

def RedLedOn():
    redLed.on()

def RedLedOff():
    redLed.off()

def SetButton1Callback(callback):
    button1.when_pressed = callback

def SetButton2Callback(callback):
    button2.when_pressed = callback