import os 
import cv2
import time
import numpy as np

# import os

from datetime import datetime
from constant import constant


class Cv2Video:
    def __init__(self, cap, fourcc, out):
        self.cap = cap
        self.fourcc = fourcc
        self.out = out
    
    def Create(self, start, out):
        out = cv2.VideoWriter('output{}.avi'.format(constant.time_string()), fourcc, 20.0, (640, 480))
        while(self.cap.isOpened()):
            # start_time = time.time()
            ret, frame = self.cap.read()
            end = time.time()
            if ret == True & (end - start) < 5.0:
                # end_time = time.time()
                # if end_time - start_time <:
                #     pass
                frame = cv2.flip(frame, 0)
                out.write(frame)
                # cv2.imshow('frame', frame)
                # if cv2.waitKey(1) & 0xFF == ord('q'):
                #     break
            else:
                break
    
    def ReleaseObj(self):
        self.cap.release()
        self.out.release()
        cv2.destroyAllWindows()

cap = cv2.VideoCapture(0)

# define the codec and create VideoWriter object 
fourcc = cv2.VideoWriter_fourcc(*'XVID')
# out = cv2.VideoWriter('output.avi', fourcc, 20.0, (640, 480))
# out = cv2.VideoWriter('output{}.avi'.format(constant.time_string()), fourcc, 20.0, (640, 480))
out = cv2.VideoWriter(os.path.join(os.getcwd(),"media",'output{}.avi'.format(constant.time_string())), fourcc, 20.0, (640, 480))

while(cap.isOpened()):
    ret, frame = cap.read()
    if ret == True:
        frame = cv2.flip(frame,0)
        out.write(frame)
        cv2.imshow('frame', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break

cap.release()
out.release()
cv2.destroyAllWindows()
