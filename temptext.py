import numpy as np
import cv2

last_t = None

def lasttemp():
    
    with open('sensortemp.txt') as f:
        for line in f:
            pass
        global last_line
        last_line = line
        
        
        return last_line
    
last_t = lasttemp()
        
