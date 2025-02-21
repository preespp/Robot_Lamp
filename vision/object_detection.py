import cv2
import numpy as np
from utils.config import MODEL_CONFIG, MODEL_WEIGHTS
from sensors.camera import Camera

class ObjectDetection:
    def __init__(self):
        self.net = cv2.dnn.readNetFromCaffe(MODEL_CONFIG, MODEL_WEIGHTS)
        self.camera = Camera()

    def detect_book(self):
        frame = self.camera.read_frame()

        if frame is None:
            return None

        blob = cv2.dnn.blobFromImage(frame, 0.007843, (300, 300), 127.5, 127.5, 127.5, True)
        self.net.setInput(blob)
        detections = self.net.forward()

        for i in range(detections.shape[2]):
            confidence = detections[0, 0, i, 2]
            if confidence > 0.5:
                class_id = int(detections[0, 0, i, 1])
                print(f"Detected class ID: {class_id}, Confidence: {confidence}")
                
                x1 = int(detections[0, 0, i, 3] * frame.shape[1])
                y1 = int(detections[0, 0, i, 4] * frame.shape[0])
                x2 = int(detections[0, 0, i, 5] * frame.shape[1])
                y2 = int(detections[0, 0, i, 6] * frame.shape[0])
                return ((x1 + x2) // 2, (y1 + y2) // 2)
        return None
