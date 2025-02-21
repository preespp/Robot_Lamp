import neopixel
from utils.config import LED_PIN, NUM_PIXELS
import smbus
import serial
import time

class Sensor:
    def __init__(self):
        self.pixels = neopixel.NeoPixel(LED_PIN, NUM_PIXELS, brightness=0.5, auto_write=False)
        self.ser = serial.Serial('/dev/ttyUSB0', 9600)  # Adjust for USB/UART port

    def update_led(self):
        if self.ser.in_waiting > 0:
            temperature = self.ser.readline().decode('utf-8').strip()  # Read temperature
            
            if temperature:
                if temperature < 20:
                    color = (0, 0, 255)  # Blue
                elif 20 <= temperature < 30:
                    color = (0, 255, 0)  # Green
                else:
                    color = (255, 0, 0)  # Red
                
                self.pixels.fill(color)
                self.pixels.show()
        
