import time
import cv2
import numpy as np
"""
ECE 471 Duck Hunt Project Solution
Zachary Legg - V00156093

April 5, 2022
"""

# Image size should be (1024, 768, 3), but for some reason it comes transposed 
# so we transpose it to resize to (768, 1024, 3)

last_img = np.zeros((768, 1024))
toggle = 0

def GetLocation(move_type, env, current_frame):
    global last_img
    global toggle
    move_type = "absolute"
    
    #print(current_frame.shape)
    # Convert the input image from 3-channel to grey
    img_grey = cv2.cvtColor(current_frame, cv2.COLOR_BGR2GRAY)
    #Transpose image
    current_img = np.transpose(img_grey)
    last_img = last_img.astype('int8')
    current_img = current_img.astype('int8')
    
    #diff = np.subtract(1.2*current_img, last_img)
    diff = np.subtract(1*current_img, 1.3*last_img)
    diff[(diff<0)] = 0
    diff = diff.astype('uint8')
   
    h = np.where(diff == np.amax(diff))
    coordinates = []
    if np.sum(last_img) != 0:
        c = 20
        if len(h[0]) > 0 and len(h[1]) > 0:
            coordinates.append({'coordinate' : (h[1][0], h[0][0]), 'move_type' : move_type})
            if toggle == 5:
                coordinates.append({'coordinate' : (h[1][0] + c, h[0][0] + c), 'move_type' : move_type})
                coordinates.append({'coordinate' : (h[1][0] + c, h[0][0] - c), 'move_type' : move_type})
                coordinates.append({'coordinate' : (h[1][0] - c, h[0][0] + c), 'move_type' : move_type})
                coordinates.append({'coordinate' : (h[1][0] - c, h[0][0] - c), 'move_type' : move_type})
                toggle = 0 
            else:
                toggle = toggle + 1
            #coordinates.append({'coordinate' : (width, height), 'move_type' : "absolute"})
           
    last_img = current_img
    return coordinates
