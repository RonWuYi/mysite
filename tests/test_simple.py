import os
import sys

from os.path import dirname, abspath

sys.path.insert(0, os.path.join(dirname(dirname(abspath(__file__))), 'myinit'))

from mytest import isSameTree, TreeNode


def test_isSameTree():
    assert isSameTree([1, 2, 3], [1, 2, 3]) == True
    
def test_isSameTree2():
    assert isSameTree([1, 2], [1, None, 3]) == False
    


if __name__ == '__main__':
    pass