import time
import cv2
import numpy as np
"""
Replace following with your own algorithm logic

Two random coordinate generator has been provided for testing purposes.
Manual mode where you can use your mouse as also been added for testing purposes.
"""

# Image size should be (1024, 768, 3), but for some reason it comes transposed 
# so we transpose it to resize to (768, 1024, 3)

last_img = np.zeros((768, 1024))

def GetLocation(move_type, env, current_frame):
    global last_img
    move_type = "absolute"
    #time.sleep(1) #artificial one second processing time
    
    #im_rgb = cv2.cvtColor(current_frame, cv2.COLOR_RGB2BGR)
    print(current_frame.shape)
    img_grey = cv2.cvtColor(current_frame, cv2.COLOR_BGR2GRAY)
    current_img = np.transpose(img_grey)
    #current_img = cv2.medianBlur(current_img,9)
    last_img = last_img.astype('int8')
    current_img = current_img.astype('int8')
    diff = np.subtract(1.2*current_img, last_img)
    diff[(diff<0)] = 0
    diff = diff.astype('uint8')
    
    #diff[diff>=210] = 0
    #diff[diff<=100] = 0
    #h = np.where((diff>110)&(diff<120))
    h = np.where(diff == np.amax(diff))
    #h = np.where((diff>=230))
    #th = 255
    #while len(h) > 5:
    	#th = th - 1
    	#h = np.where((diff>=230) & (diff<=th))
#    print(h)
    coordinates = []
    if np.sum(last_img) != 0:
        c = 10
        d = 20
        m1 = 1
        m2 = 2
        #for i in range(len(h[0])):
        if len(h[0]) > 0 and len(h[1]) > 0:
            #coordinates.append({'coordinate' : (h[1][0], h[0][0] + c), 'move_type' : move_type})
            #coordinates.append({'coordinate' : (h[1][0], h[0][0] - c), 'move_type' : move_type})
            
            #coordinates.append({'coordinate' : (h[1][0] + m1*c, h[0][0] + m1*c), 'move_type' : move_type})
            #coordinates.append({'coordinate' : (h[1][0] - m1*c, h[0][0] - m1*c), 'move_type' : move_type})
            #coordinates.append({'coordinate' : (h[1][0] - m1*c, h[0][0] + m1*c), 'move_type' : move_type})
            #coordinates.append({'coordinate' : (h[1][0] - m1*c, h[0][0] + m1*c), 'move_type' : move_type})
            
            coordinates.append({'coordinate' : (h[1][0] + c, h[0][0] + c), 'move_type' : move_type})
            coordinates.append({'coordinate' : (h[1][0] - c, h[0][0] - c), 'move_type' : move_type})
            coordinates.append({'coordinate' : (h[1][0] - c, h[0][0] + c), 'move_type' : move_type})
            coordinates.append({'coordinate' : (h[1][0] - c, h[0][0] + c), 'move_type' : move_type})
            
            coordinates.append({'coordinate' : (h[1][0] + d, h[0][0] + d), 'move_type' : move_type})
            coordinates.append({'coordinate' : (h[1][0] - d, h[0][0] - d), 'move_type' : move_type})
            coordinates.append({'coordinate' : (h[1][0] - d, h[0][0] + d), 'move_type' : move_type})
            coordinates.append({'coordinate' : (h[1][0] - d, h[0][0] + d), 'move_type' : move_type})
            
            
            #coordinates.append({'coordinate' : (h[1][0], h[0][0] + c), 'move_type' : move_type})
            #coordinates.append({'coordinate' : (h[1][0] - c, h[0][0] + c), 'move_type' : move_type})
            #coordinates.append({'coordinate' : (h[1][0] - c, h[0][0] + c), 'move_type' : move_type})
            
            #coordinates.append({'coordinate' : (width, height), 'move_type' : "absolute"})
           
    last_img = current_img
    return coordinates
