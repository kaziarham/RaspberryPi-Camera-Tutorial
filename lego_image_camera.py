from picamera2 import Picamera2

picam2 = Picamera2()
#picam2.start_and_capture_file("images/lego_minifigures.jpg")
picam2.start_and_capture_files("images/sequence{:d}.jpg", num_files=3, delay=0.5)
picam2.close()