cmake_minimum_required(VERSION 3.10)
project(RPi_Robotics)

set(CMAKE_CXX_STANDARD 14)

find_package(OpenCV REQUIRED)
include_directories(${OpenCV_INCLUDE_DIRS})

add_executable(object_detection src/object_detection.cpp)
add_executable(led_control src/led_control.cpp)

target_link_libraries(object_detection ${OpenCV_LIBS} wiringPi)
target_link_libraries(led_control wiringPi)