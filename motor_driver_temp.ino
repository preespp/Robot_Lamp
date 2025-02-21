#include <Wire.h>
#include <Servo.h>

Servo myServo1, myServo2, myServo3;
int servobase = 9;
int servomid = 10;
int servoend = 11;

int sensorPin = A0;
int tempValue = 0;
float temperature = 0.0;

// Define I2C slave address
#define SLAVE_ADDR 0x08

void setup() {
  // Start I2C and serial communication
  Wire.begin(SLAVE_ADDR);
  Wire.onReceive(receiveEvent);
  Serial.begin(9600);  // Serial communication
  
  myServo1.attach(servobase);
  myServo2.attach(servomid);
  myServo3.attach(servoend);
}

void loop() {
  // Read the temperature sensor (LMT86LP)
  tempValue = analogRead(sensorPin);
  float voltage = tempValue * (5.0 / 1023.0);
  temperature = (voltage - 0.5) * 100;  // Convert to Celsius
  
  // Send temperature data to Raspberry Pi via serial
  Serial.print(temperature);
  Serial.println();
  
  delay(500);
}

void receiveEvent(int bytes) {
  if (bytes >= 3) {
    int angle1 = Wire.read();
    int angle2 = Wire.read();  
    int angle3 = Wire.read();  
    
    // Move the servos based on the received angles
    if (angle1 >= 0 && angle1 <= 180) {
      myServo1.write(angle1);
    }
    if (angle2 >= 0 && angle2 <= 180) {
      myServo2.write(angle2);
    }
    if (angle3 >= 0 && angle3 <= 180) {
      myServo3.write(angle3);
    }
  }
}