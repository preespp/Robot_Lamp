#include <opencv2/opencv.hpp>
#include <iostream>
#include <wiringPiI2C.h>
#include <wiringPi.h>

#define ARDUINO_ADDR 0x08  // Replace with your Arduino I2C address

using namespace cv;
using namespace std;

int main() {
    // Open the Pi Camera
    VideoCapture cap(0);
    if (!cap.isOpened()) {
        cerr << "Error: Couldn't open the camera." << endl;
        return -1;
    }

    int fd = wiringPiI2CSetup(ARDUINO_ADDR);
    if (fd == -1) {
        cerr << "Error: Couldn't initialize I2C communication." << endl;
        return -1;
    }

    Mat frame;
    while (true) {
        cap >> frame;
        if (frame.empty()) break;

        // Convert to grayscale for processing
        Mat gray;
        cvtColor(frame, gray, COLOR_BGR2GRAY);
        
        // Object detection logic (Placeholder)
        // Detect object and calculate servo angles
        int angle1 = 90, angle2 = 45, angle3 = 120;

        // Send angles to Arduino via I2C
        wiringPiI2CWriteReg8(fd, 0x01, angle1);
        wiringPiI2CWriteReg8(fd, 0x02, angle2);
        wiringPiI2CWriteReg8(fd, 0x03, angle3);

        imshow("Object Detection", frame);
        if (waitKey(1) == 27) break;  // Press 'ESC' to exit
    }

    cap.release();
    destroyAllWindows();
    return 0;
}
