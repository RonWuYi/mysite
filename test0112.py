# from func import opencvSave
import os

from constant import constant


class Image:
    def __init__(self, start_time):
        self.start_time = start_time
        self.outtest = os.path.join(os.getcwd(),"media",'output{}.avi'.format(constant.time_string())) 

    
    def my_save(self):
        return self.outtest


if __name__ == '__main__':

    from datetime import datetime
    while True:
        print(datetime.now().isoformat(timespec='seconds').replace(':', ''))
        print(type(datetime.now().isoformat(timespec='seconds')))
# >>> datetime.now().isoformat(timespec='minutes')   # doctest: +SKIP
# '2002-12-25T00:00'
    # while True:
    #     A = Image(constant.outtest)
    #     print(A.my_save())
