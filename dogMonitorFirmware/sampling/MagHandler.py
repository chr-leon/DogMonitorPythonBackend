# coding=utf-8

import smbus			#import SMBus module of I2C
from time import sleep          #import
import time
#from SQLHandler import SQLHandler
class MagHandler:

    def __init__(self, bus):        
        Register_A     = 0              #Address of Configuration register A
        Register_B     = 0x01           #Address of configuration register B
        Register_mode  = 0x02           #Address of mode register

        X_axis_H    = 0x03              #Address of X-axis MSB data register
        Z_axis_H    = 0x05              #Address of Z-axis MSB data register
        Y_axis_H    = 0x07              #Address of Y-axis MSB data register


        self.Device_Address = 0x1E   # MPU6050 device address
        self.bus = bus 

    def connect(self):        
        try:
            #write to Configuration Register A
            self.bus.write_byte_data(self.Device_Address, self.Register_A, 0x70)

            #Write to Configuration Register B for gain
            self.bus.write_byte_data(self.Device_Address, self.Register_B, 0xa0)

            #Write to mode Register for selecting mode
            self.bus.write_byte_data(self.Device_Address, self.Register_mode, 0)
        except:
            return False
        return True

    def read_raw_data(self, addr):
         #Read raw 16-bit value
        high = self.bus.read_byte_data(self.Device_Address, addr)
        low = self.bus.read_byte_data(self.Device_Address, addr+1)

        #concatenate higher and lower value
        value = ((high << 8) | low)

        #to get signed value from module
        if(value > 32768):
            value = value - 65536
        return value        

    def get_one_sample(self):
        x = self.read_raw_data(self.X_axis_H)
        z = self.read_raw_data(self.Z_axis_H)
        y = self.read_raw_data(self.Y_axis_H)
        
        return [0, x, y, z]