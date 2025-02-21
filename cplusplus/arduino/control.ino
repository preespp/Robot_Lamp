#include <Wire.h>
#include <Servo.h>

Servo servo1, servo2, servo3;

void setup() {
    Wire.begin(0x08);  // Set I2C address
    Wire.onReceive(receiveEvent);
    
    servo1.attach(9);
    servo2.attach(10);
    servo3.attach(11);
}

void receiveEvent(int bytes) {
    while (Wire.available()) {
        byte reg = Wire.read();
        byte angle = Wire.read();

        if (reg == 0x01) servo1.write(angle);
        else if (reg == 0x02) servo2.write(angle);
        else if (reg == 0x03) servo3.write(angle);
    }
}

void loop() {
    delay(10);
}
