from picamera2 import Picamera2
import time
import cv2

picam2 = Picamera2()

# Set the resolution
picam2.preview_configuration.size = (2592, 1944)
picam2.start(show_preview=True)

# Show the preview for 2 seconds
time.sleep(2)

# Save the image and close the camera
picam2.capture_file("images/lego_original2.jpg")
picam2.close()

# Read the image
img = cv2.imread("images/lego_original2.jpg")

# Convert to negative
greyscale = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imwrite("images/lego_negative.jpg", 255 - greyscale)