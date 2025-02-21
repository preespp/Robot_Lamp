import threading
import time
from sensors.temp_sensor import Sensor
from vision.tracking import Tracking

if __name__ == "__main__":
    temp_sensor = Sensor()
    tracking = Tracking()

    t1 = threading.Thread(target=temp_sensor.update_led)
    t2 = threading.Thread(target=tracking.track_book)

    t1.start()
    t2.start()

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print("Shutting down...")