# from . import MyData

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
# print(MyData.name)

def isSameTree(p: TreeNode, q: TreeNode) -> bool:
    def t(n):
        return n and (n.val, t(n.left), t(n.right))

    return t(p) == t(q)

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        if len(nums) < 2:
            return None
        elif len(nums) == 2 and sum(nums) == target:
            return [0, 1]
        else:
            for i in range(len(nums)):
                for j in range(len(nums[i+1:])):
                    if nums[i] + nums[i+1:][j] == target:
                        return [i, i+1+j]

