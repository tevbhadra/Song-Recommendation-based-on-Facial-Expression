#!/usr/bin/env python2
# -*- coding: utf-8 -*-


import cv2
import numpy as np

def capture_image():
    basedir='/Users/bhadra/Documents/PSU Study Mat/Fall-II/Deep Learning/Project/'
    camera = cv2.VideoCapture(0)
    raw_input('Press Enter to capture')
    return_value, image = camera.read()
    path_to_image = basedir+'image_'+str(int(np.random.rand()*10))+'.png'    
    cv2.imwrite(path_to_image, image)
    del(camera)
    return path_to_image