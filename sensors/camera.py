import cv2
from utils.config import CAMERA_INDEX

class Camera:
    def __init__(self):
        self.cap = cv2.VideoCapture(CAMERA_INDEX)

    def read_frame(self):
        ret, frame = self.cap.read()
        return frame if ret else None

    def release(self):
        self.cap.release()
