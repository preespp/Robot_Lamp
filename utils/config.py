import board

# GPIO Pins
SERVO_PINS = [17, 18, 27]
TEMP_SENSOR_PIN = 4
LED_PIN = board.D18
NUM_PIXELS = 30

# Object Detection Model Paths
MODEL_CONFIG = "deploy.prototxt"
MODEL_WEIGHTS = "mobilenet_iter_73000.caffemodel"

# Camera Configuration
CAMERA_INDEX = 0