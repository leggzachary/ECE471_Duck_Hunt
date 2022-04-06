import time
import cv2
import numpy as np
"""
ECE 471 Duck Hunt Project Solution
Zachary Legg - V00156093

April 6, 2022
"""

# Image size should be (1024, 768, 3), but for some reason it comes transposed 
# so we transpose it to resize to (768, 1024, 3)

last_img = np.zeros((768, 1024))
crosshair_loc = [0, 0] #(width, height)
def GetLocation(move_type, env, current_frame):
    global last_img
    global crosshair_loc
    move_type = "absolute"
    
    #print(current_frame.shape)
    # Convert the input image from 3-channel to grey
    img_grey = cv2.cvtColor(current_frame, cv2.COLOR_BGR2GRAY)
    #Transpose image
    current_img = np.transpose(img_grey)
    last_img = last_img.astype('int32')
    current_img = current_img.astype('int32')
    
    xmin = 0
    xmax = 0
    xmin = crosshair_loc[0] - 20
    if xmin < 0:
        xmin = 0
        xmax = crosshair_loc[0] + 40
    else:
        xmax = crosshair_loc[0] + 20
        if xmax > 1023:
            xmax = 1023
            xmin = crosshair_loc[0] - 40
        
    ymin = 0
    ymax = 0
    ymin = crosshair_loc[1] - 20
    if ymin < 0:
        ymin = 0
        ymax = crosshair_loc[1] + 40
    else:
        ymax = crosshair_loc[1] + 20
        if ymax > 767:
            ymax = 767
            ymin = crosshair_loc[1] - 40
    
    #last_img [ymin:ymax, xmin:xmax] = 255
    
    #diff = np.subtract(1.2*current_img, last_img)
    diff = np.subtract(1*last_img, 1*current_img)
    diff [ymin:ymax, xmin:xmax] = 0
    
    
    #print(diff[767,1023])        
    diff[diff<0] = 0
    
    diff = diff.astype('uint8')
    #cv2.imwrite("./diff.jpg", diff)
    #cv2.imwrite("./curr.jpg", current_img.astype('uint8'))
    #cv2.imwrite("./last.jpg", last_img.astype('uint8'))
    h = np.where(diff == np.amax(diff))
    coordinates = []
    if np.sum(last_img) != 0:
        c = 20
        d = 40
        if len(h[0]) > 0 and len(h[1]) > 0:
            coordinates.append({'coordinate' : (h[1][0], h[0][0]), 'move_type' : move_type})

            coordinates.append({'coordinate' : (h[1][0] + c, h[0][0] + c), 'move_type' : move_type})
            coordinates.append({'coordinate' : (h[1][0] + c, h[0][0] - c), 'move_type' : move_type})
            coordinates.append({'coordinate' : (h[1][0] - c, h[0][0] + c), 'move_type' : move_type})
            coordinates.append({'coordinate' : (h[1][0] - c, h[0][0] - c), 'move_type' : move_type})
            
            coordinates.append({'coordinate' : (h[1][0] + d, h[0][0] + d), 'move_type' : move_type})
            coordinates.append({'coordinate' : (h[1][0] + d, h[0][0] - d), 'move_type' : move_type})
            coordinates.append({'coordinate' : (h[1][0] - d, h[0][0] + d), 'move_type' : move_type})
            coordinates.append({'coordinate' : (h[1][0] - d, h[0][0] - d), 'move_type' : move_type})
            
            crosshair_loc[0] = h[1][0]- d
            crosshair_loc[1] = h[0][0]- d
        else:
            crosshair_loc[0] = 100
            crosshair_loc[1] = 100
        

           
    last_img = current_img
    return coordinates
