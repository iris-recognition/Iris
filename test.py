from picamera import PiCamera
from time import sleep
from time import time
from scipy.io import savemat
import os
import cv2
from fnc.extractFeature import extractFeature

camera = PiCamera()

camera.start_preview()
camera.brightness=60
sleep(10)
           
camera.stop_preview()

#a='/home/pi/Downloads/Iris-RecextractFeatureognition-master/python/img'+d+'jpg'
camera.capture('/home/pi/Downloads/Iris-Recognition-master/python/data6/img1.jpg')
img=cv2.imread('/home/pi/Downloads/Iris-Recognition-master/python/data6/img1.jpg',0)
cv2.imwrite('/home/pi/Downloads/Iris-Recognition-master/python/data6/img1.png',img)
cv2.imshow('image',img)
cv2.waitKey(0)
file='/home/pi/Downloads/Iris-Recognition-master/python/data6/img1.png'
print('>>> Enroll for the file ', file)
file = extractFeature(file)

# Save extracted feature
basename = os.path.basename(file)

out_file = os.path.join('/home/pi/Downloads/Iris-Recognition-master/python/templates/data6', "%s.mat" % (basename))
savemat(out_file, mdict={'template':file, 'mask':file})
print('>>> Template is saved in %s' % (out_file))
#cv2.waitKey(0)