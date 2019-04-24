from picamera import PiCamera
from time import sleep
from time import time
from scipy.io import savemat
import os
import cv2
from fnc.extractFeature import extractFeature

camera = PiCamera()
for n in range(1,9):
    camera.start_preview()
    camera.brightness=60
    sleep(2)
           
    camera.stop_preview()

#a='/home/pi/Downloads/Iris-RecextractFeatureognition-master/python/img'+d+'jpg'
    list = os.listdir('/home/pi/Downloads/Iris-Recognition-master/python/data') # dir is your directory path
    number_files = len(list)
    i=(int)((number_files/2)+1)
    string='img'+str(i)
    camera.capture('/home/pi/Downloads/Iris-Recognition-master/python/data/'+string+'.jpg')
    img=cv2.imread('/home/pi/Downloads/Iris-Recognition-master/python/data/'+string+'.jpg',0)
    cv2.imwrite('/home/pi/Downloads/Iris-Recognition-master/python/data/'+string+'.png',img)
    cv2.imshow('image',img)
    cv2.waitKey(0)
    file='/home/pi/Downloads/Iris-Recognition-master/python/data/'+string+'.jpg'
    print('>>> Enroll for the file ', file)
    template, mask, file = extractFeature(file)
    print()
##cv2.imshow('imag1',template)
##cv2.imshow('image',mask)
    print("d")

# Save extracted feature
    #basename =s
    
#basename ='data'+i
    out_file = os.path.join('/home/pi/Downloads/Iris-Recognition-master/python/temp/', "%s.mat" % (string))
    savemat(out_file, mdict={'template':template, 'mask':mask})
    print('>>> Template is saved in %s' % (out_file))
#cv2.waitKey(0)

