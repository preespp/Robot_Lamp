import time
from vision.object_detection import ObjectDetection
from robot_arm.inverse_kinematics import compute_ik
from robot_arm.motor_control import move_robot_arm

class PositionTracking:
    def __init__(self):
        self.detector = ObjectDetection()
        self.prev_position = None

    def track_book(self):
        while True:
            book_position = self.detector.detect_book()
            if book_position and self.prev_position:
                dx = book_position[0] - self.prev_position[0]
                dy = book_position[1] - self.prev_position[1]

                print(f"Book moved: Δx={dx}, Δy={dy}")
                angles = compute_ik(dx, dy)
                move_robot_arm(angles)

            self.prev_position = book_position
            time.sleep(0.1)
