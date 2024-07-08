from picamera2 import Picamera2
import time

picam2 = Picamera2()

# Set preview resolution at a lower resolution
picam2.preview_configuration.sensor.output_size = (2592, 1944)
picam2.preview_configuration.main.size = (800, 600)
picam2.configure("preview")
picam2.start(show_preview=True)

# Preview for 2 seconds
time.sleep(2)

picam2.capture_file("images/lego_lores.jpg") # Lower resolution
picam2.close()