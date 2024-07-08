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
picam2.capture_file("images/lego_original3.jpg")
picam2.close()

# Read the image
img = cv2.imread("images/lego_original3.jpg")

# Convert to sketch
greyscale = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
inverted = 255 - greyscale
blur_inverted = cv2.GaussianBlur(inverted, (125, 125), 0)
inverted_blur = 255 - blur_inverted
sketch = cv2.divide(greyscale, inverted_blur, scale=256)
cv2.imwrite("images/lego_sketch.jpg", sketch)