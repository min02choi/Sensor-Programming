import picamera
import time

camera = picamera.PiCamera()
camera. resolution = (1920, 1080)   # (64, 64) ~ (1920, 1080) px
camera. framerate = 30              # 1 ~ 30 fps

print("Now starting to save a movie clip")
camera.start_recording("video_test.h264")
time.sleep(10)
camera.stop_recording()
