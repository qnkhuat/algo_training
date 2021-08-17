# https://leetcode.com/problems/sort-colors/
from typing import List

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        if len(nums) < 2: return nums

        p, p1, p2 = 0, 0, len(nums) - 1
        while p <= p2:
            if nums[p] == 0:
                nums[p], nums[p1] = nums[p1], nums[p]
                p1 += 1
                p += 1
            elif nums[p] == 2:
                nums[p], nums[p2] = nums[p2], nums[p]
                p2 -= 1
            else:
                p += 1 
        return nums

        
def test(args, expect):
    output = Solution().sortColors(*args)
    print(f"{output == expect} case: {args}, output: {output}, expect: {expect} ")


test([[2,0,2,1,1,0]], [0,0,1,1,2,2])
test([[2,0,1]], [0,1,2])
test([[0]], [0])
test([[1]], [1])
