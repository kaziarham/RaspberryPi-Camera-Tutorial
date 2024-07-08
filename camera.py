from picamera2 import Picamera2, Preview
import time
from libcamera import Transform

# The camera preview should be shown for 5 seconds and close the preview
picam2 = Picamera2()
picam2.start_preview(Preview.QTGL, transform=Transform(hflip=True, vflip=True))
picam2.start()
time.sleep(5)
picam2.close()