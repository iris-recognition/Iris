from picamera import PiCamera
import time

#camera = PiCamera()   

camera = PiCamera()
##        camera.brightness = 70

camera.start_preview()
camera.brightness = 70
time.sleep(10)
camera.capture('/home/pi/Desktop/image.jpg')
camera.stop_preview()
#camera.start_recording('/home/pi/video.h264')
##sleep(10)
##camera.capture('/home/pi/Desktop/image.jpg')
##camera.stop_recording()
##camera.stop_preview()
