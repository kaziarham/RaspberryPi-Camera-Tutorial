from picamera2 import Picamera2

picam2 = Picamera2()
picam2.start_and_record_video("videos/lego_minifigures.mp4", duration=5, show_preview=True)
picam2.close()