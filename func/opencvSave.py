import os 
import cv2
import time
import numpy as np

# import os

from datetime import datetime
from constant import constant


class Cv2Video:
    def __init__(self, cap, fourcc):
        self.cap = cap
        self.fourcc = fourcc
        self.out = cv2.VideoWriter(os.path.join(os.getcwd(),"media",'output{}.avi'.format(constant.time_string())), self.fourcc, 20.0, (640, 480))
        self.start_time = time.time()
    
    def Create(self):
        # start = time.time()
        # out = cv2.VideoWriter('output{}.avi'.format(time_string), fourcc, 20.0, (640, 480))
        while(self.cap.isOpened()):
            # start_time = time.time()
            ret, frame = self.cap.read()
            end = time.time()
            time_diff = end - self.start_time
            if ret == True and (time_diff) <= 5.0:
                # end_time = time.time()
                # if end_time - start_time <:
                #     pass
                frame = cv2.flip(frame, 0)
                self.out.write(frame)
                # cv2.imshow('frame', frame)
                # if cv2.waitKey(1) & 0xFF == ord('q'):
                #     break
            else:
                # self.cap.release()
                # self.out.release()
                # cv2.destroyAllWindows()
                break
    
    def ReleaseObj(self):
        self.cap.release()
        self.out.release()
        cv2.destroyAllWindows()

# cap = cv2.VideoCapture(0)

# # define the codec and create VideoWriter object 
# fourcc = cv2.VideoWriter_fourcc(*'XVID')
# # out = cv2.VideoWriter('output.avi', fourcc, 20.0, (640, 480))
# # out = cv2.VideoWriter('output{}.avi'.format(constant.time_string()), fourcc, 20.0, (640, 480))
# out = cv2.VideoWriter(os.path.join(os.getcwd(),"media",'output{}.avi'.format(constant.time_string())), fourcc, 20.0, (640, 480))

# while(cap.isOpened()):
#     ret, frame = cap.read()
#     if ret == True:
#         frame = cv2.flip(frame,0)
#         out.write(frame)
#         cv2.imshow('frame', frame)
#         if cv2.waitKey(1) & 0xFF == ord('q'):
#             break
#     else:
#         break

# cap.release()
# out.release()
# cv2.destroyAllWindows()
