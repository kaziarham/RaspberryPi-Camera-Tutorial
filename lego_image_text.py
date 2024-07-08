from picamera2 import Picamera2, MappedArray
import cv2
import time

resolution = (2592, 1944)

# Function to give text options
def apply_text(request):
    colour = (255, 255, 255)
    origin = (0, 60)
    font = cv2.FONT_HERSHEY_SIMPLEX
    scale = 2
    thickness = 2
    text = time.strftime("%Y-%m-%d %X")
    with MappedArray(request, "main") as m:
        cv2.putText(m.array, text, origin, font, scale, colour, thickness)

# Create camera object
picam2 = Picamera2()

'''
Create two separate configurations - one for preview and one for capture.
Make sure the preview is the same resolution as the capture, to make sure the overlay stays the same size
'''
capture_config = picam2.create_still_configuration({"size": resolution})
preview_config = picam2.create_preview_configuration({"size": resolution})

# Set the current config as the preview config
picam2.configure(preview_config)

# Add the text
picam2.pre_callback = apply_text

# Start the camera and show the preview for 2 seconds
picam2.start(show_preview=True)
time.sleep(2)

# Switch to the capture config and then take a picture
image = picam2.switch_mode_and_capture_file(capture_config, "images/timestampOnLego.jpg")

# Close the camera
picam2.close()