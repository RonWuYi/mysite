import os
import sys
from pathlib import Path
from os.path import dirname, abspath

sys.path.insert(0, os.path.join(dirname(dirname(abspath(__file__))), 'myinit'))

def return_path():
    return sys.path[0]


def test_return_path():
    assert return_path() == '/home/hdc/project/github/mysite/myinit'
    
if __name__ == '__main__':
    # for i in Path.cwd().parents:
    #     print(i)
    # from os.path import dirname, abspath
    # d = dirname(dirname(abspath(__file__)))
    # print(d)
    # print(type(d))
    for i in sys.path:
        print(i)
        
        