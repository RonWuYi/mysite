import time

from random import randint
from func.wrapperTest import timethis

def print_random(start_time, myflag=True):
    # start = time.time()
    while myflag:
        end = time.time()
        if end-start >3.0:
            myflag = False
        if myflag != False:
            print(randint(0, 10000))
            time.sleep(1)
        # else:
        #     break

if __name__ == '__main__':
    start = time.time()
    while True:
        print_random(start)
    # @timethis
    # print_random()
