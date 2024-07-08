from picamera2 import Picamera2
import time

picam2 = Picamera2()

# Set the resolution
# picam2.preview_configuration.size = (2592, 1944) # Maximum resolution
picam2.preview_configuration.size = (64, 64) # Minimum resolution
picam2.start(show_preview=True)

# Preview for 2 seconds
time.sleep(2)

# Take the picture
# picam2.capture_file("images/lego_max.jpg") # Maximum resolution
picam2.capture_file("images/lego_min.jpg") # Minimum resolution
picam2.close()