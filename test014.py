import os
import cv2
import time

from pathlib import Path
from func import opencvSave
from threading import Thread
from constant import constant, google

google.set_env()
keyFlag = True

my_save = opencvSave.Cv2Video(constant.cap, constant.fourcc)

t1 = Thread(target=my_save.Create, args=())
t2 = Thread(target=my_save.Upload, args=(os.path.join(str(Path.cwd()), 'media'), ))
t1.start()
t2.start()
t2.join()
t1.join()

countdown = 100
while keyFlag:
    countdown -= 1
    if countdown == 0:
        keyFlag = False
        # t1.s



