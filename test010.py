import time

from random import randint
from func.wrapperTest import timethis

def print_random():
    while True:
        print(randint(0, 10000))
        time.sleep(1)

if __name__ == '__main__':
    # print_random()
    @timethis
    print_random()
