import numpy as np
import cv2
import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler



class MyHandler(FileSystemEventHandler):

    
    def on_modified(self, event):
        last_t = None

        def lasttemp():
            
            with open('sensortemp.txt') as f:
                for line in f:
                    pass
                
                    last_temp = line
                
                
            return last_temp
            
        last_t = lasttemp()

        print(last_t)
        
        
        
        
        

        
        
event_handler = MyHandler()
observer = Observer()
observer.schedule(event_handler, path='/home/pi/PrevenFrontEnd', recursive=False)
observer.start()
try:
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    observer.stop()
observer.join()




        
