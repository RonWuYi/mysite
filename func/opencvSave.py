import os 
import cv2
import time
import numpy as np

from datetime import datetime
from constant import constant, google


class Cv2Video:
    def __init__(self, cap, fourcc):
        self.cap = cap
        self.fourcc = fourcc
        self.out = cv2.VideoWriter(os.path.join(os.getcwd(),"media",'output{}.avi'.format(constant.time_string())), self.fourcc, 20.0, (640, 480))
        self.start_time = time.time()
    
    def Create(self):
        while(self.cap.isOpened()):
            ret, frame = self.cap.read()
            # cv2.imshow('frame', frame)
            end = time.time()
            time_diff = end - self.start_time
            if ret == True and (time_diff) <= 5.0:
                frame = cv2.flip(frame, 0)
                # cv2.imshow('frame', frame)
                self.out.write(frame)
                # cv2.imshow('frame', frame)
            else:
                break
    
    def Upload(self, folder):
        for i in os.listdir(os.path.join(folder, 'media')):
            if i.endswith('avi'):
                print(i)
                google.upload_blob(constant.storage_name, os.path.join(folder, 'media', i), 'test{}'.format(i))

    def ReleaseObj(self):
        self.cap.release()
        self.out.release()
        cv2.destroyAllWindows()
