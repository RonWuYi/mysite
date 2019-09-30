import cv2
import time

from func import opencvSave
from constant import constant

cap = cv2.VideoCapture(0)

# define the codec and create VideoWriter object 
fourcc = cv2.VideoWriter_fourcc(*'XVID')
# out = cv2.VideoWriter('output.avi', fourcc, 20.0, (640, 480))
out = cv2.VideoWriter('output{}.avi'.format(constant.time_string()), fourcc, 20.0, (640, 480))

save_count = 0
while True:
    start_time = time.time()
    # my_save = opencvSave.Cv2Video(cap, fourcc, out)
    # my_save.Create(start_time)

    my_save = opencvSave.Cv2Video(cap, fourcc)
    my_save.Create(start_time, out)
    save_count += 1
    my_save.release()
    if save_count >= 5:
        break


