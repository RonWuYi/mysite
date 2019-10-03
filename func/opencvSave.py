import os 
import cv2
import time
import numpy as np

from pathlib import Path
from datetime import datetime
from constant import constant, google


class Cv2Video:
    def __init__(self, cap, fourcc):
        self.cap = cap
        self.fourcc = fourcc
        self.fileName = 'out{}.avi'.format(constant.time_string())
        self.out = cv2.VideoWriter(os.path.join(str(Path.cwd()), 'media', self.fileName), self.fourcc, 20.0, (640, 480))
        self.start_time = time.time()
        self._Createrunning = True
        self._Uploadrunning = True
    
    def terminateCreat(self):
        self._Createrunning = False
        # self._running = False

    def terminateCreat(self):
        self._Uploadrunning = False

    def Create(self):
        frame_count = 120
        while(self.cap.isOpened() and self._Createrunning == True):
            ret, frame = self.cap.read()
            if ret == True and (frame_count) > 0:
                frame = cv2.flip(frame, 0)
                self.out.write(frame)
                frame_count -= 1
            else:
                frame_count = 120
                self.out=cv2.VideoWriter(os.path.join(str(Path.cwd()), 'media', 'out{}.avi'.format(constant.time_string())), self.fourcc, 20.0, (640, 480))
                break
    
    def Upload(self, folder):
        upload_file = []
        while self._Uploadrunning:
            # for i in os.listdir(os.path.join(folder, 'media')):
            for i in os.listdir(folder):
                if i.endswith('avi'):
                    if i not in upload_file:
                        # pass
                        google.upload_blob(constant.storage_name, os.path.join(folder, i), 'test{}'.format(i))
                        upload_file.append(i)

    def ReleaseObj(self):
        self.cap.release()
        self.out.release()
        # cv2.destroyAllWindows()
