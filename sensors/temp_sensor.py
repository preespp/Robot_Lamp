import time
import Adafruit_DHT
import neopixel
from utils.config import TEMP_SENSOR_PIN, LED_PIN, NUM_PIXELS

class TemperatureSensor:
    def __init__(self):
        self.sensor = Adafruit_DHT.DHT22
        self.pixels = neopixel.NeoPixel(LED_PIN, NUM_PIXELS, brightness=0.2, auto_write=False)

    def update_led(self):
        while True:
            humidity, temperature = Adafruit_DHT.read_retry(self.sensor, TEMP_SENSOR_PIN)
            if temperature:
                if temperature < 20:
                    color = (0, 0, 255)  # Blue (Cold)
                elif 20 <= temperature < 30:
                    color = (0, 255, 0)  # Green (Moderate)
                else:
                    color = (255, 0, 0)  # Red (Hot)
                
                self.pixels.fill(color)
                self.pixels.show()
            
            time.sleep(5)
