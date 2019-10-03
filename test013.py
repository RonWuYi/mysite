import os
import cv2
import time

from func import opencvSave
from threading import Thread
from constant import constant, google

save_count = 0
while True:
    my_save = opencvSave.Cv2Video(constant.cap, constant.fourcc)
    my_save.Create()
    save_count += 1

    if save_count >= 5:
        my_save.ReleaseObj()
        break

media_folder = 'C:\\Work\\test project\\github\\mysite\\media'
for i in os.listdir():
    if i.endswith('avi'):
        print(i)
        google.upload_blob(constant.storage_name, os.path.join(media_folder, i), 'test{}'.format(i))

    


