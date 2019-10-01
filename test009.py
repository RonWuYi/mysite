import os
import cv2
import time

from func import opencvSave
from constant import constant

# cap = cv2.VideoCapture(0)

# # define the codec and create VideoWriter object 
# fourcc = cv2.VideoWriter_fourcc(*'XVID')
# # out = cv2.VideoWriter('output.avi', fourcc, 20.0, (640, 480))
# out = cv2.VideoWriter('output{}.avi'.format(constant.time_string()), fourcc, 20.0, (640, 480))


save_count = 0
while True:
    # start_time = time.time()
    # cur_string = constant.time_string()
    # out = cv2.VideoWriter(os.path.join(os.getcwd(),"media",'output{}.avi'.format(constant.time_string())), constant.fourcc, 20.0, (640, 480))
    # my_save = opencvSave.Cv2Video(cap, fourcc, out)
    # my_save.Create(start_time)

    # my_save = opencvSave.Cv2Video(constant.cap, constant.fourcc, out=out)
    my_save = opencvSave.Cv2Video(constant.cap, constant.fourcc)
    # my_save.Create(start_time, cur_string=cur_string)
    my_save.Create()
    save_count += 1

    if save_count >= 5:
        my_save.ReleaseObj()
        break
    


