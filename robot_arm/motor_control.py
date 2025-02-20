import time
import RPi.GPIO as GPIO
from utils.config import SERVO_PINS

class MotorControl:
    def __init__(self):
        GPIO.setmode(GPIO.BCM)
        for pin in SERVO_PINS:
            GPIO.setup(pin, GPIO.OUT)
    
    def move_robot_arm(self, angles):
        for i in range(4):
            pwm = GPIO.PWM(SERVO_PINS[i], 50)
            pwm.start(0)
            duty_cycle = angles[i] / 18 + 2
            pwm.ChangeDutyCycle(duty_cycle)
            time.sleep(0.5)
            pwm.stop()

    def cleanup(self):
        GPIO.cleanup()
