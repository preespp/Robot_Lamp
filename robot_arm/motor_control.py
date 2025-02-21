import time
from smbus2 import SMBus

class MotorControl:
    def __init__(self):
        # Set up I2C
        self.bus = SMBus(1)  # Chaning I2C Bus
        self.address = 0x08  # I2C address of Arduino
    
    def move_robot_arm(self, angles):
        # Send servo angles over I2C to Arduino
        self.send_angles_i2c(angles)

    def send_angles_i2c(self, angles):
        # Send angles to Arduino via I2C as 3 bytes
        if len(angles) == 3:
            # Ensure that the angles are within valid range
            for i in range(3):
                if (0 > angles[i]):
                    angles = 0
                if (180 < angles[i]):
                    angles = 180

            # Write the angles as a list of bytes to Arduino
            self.bus.write_i2c_block_data(self.address, 0, angles)
            time.sleep(0.1)
