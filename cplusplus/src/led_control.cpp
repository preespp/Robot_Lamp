#include <iostream>
#include <fstream>
#include <wiringPi.h>
#include <wiringSerial.h>

using namespace std;

#define SERIAL_PORT "/dev/serial0"
#define LED_PIN 18  // Replace with actual LED pin

int main() {
    int serial_fd = serialOpen(SERIAL_PORT, 9600);
    if (serial_fd == -1) {
        cerr << "Error: Couldn't open serial port." << endl;
        return -1;
    }

    wiringPiSetup();
    pinMode(LED_PIN, PWM_OUTPUT);

    while (true) {
        if (serialDataAvail(serial_fd)) {
            string tempData;
            char c;
            while (serialDataAvail(serial_fd)) {
                c = serialGetchar(serial_fd);
                if (c == '\n') break;
                tempData += c;
            }

            float temperature = stof(tempData);
            int brightness = min(255, max(0, int(temperature * 10)));  // Example mapping
            pwmWrite(LED_PIN, brightness);

            cout << "Temperature: " << temperature << "°C, LED Brightness: " << brightness << endl;
        }
    }

    serialClose(serial_fd);
    return 0;
}
