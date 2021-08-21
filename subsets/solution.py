# https://leetcode.com/problems/subsets/
from typing import List

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = [[]]
        self.build(nums, result)
        return result

    def build(self, stack: List[int], result: List[List[int]]): 
        if len(stack) == 0 : return
        num = stack.pop(0)
        tempResult = []
        for arr in result:
            temp = arr.copy()
            temp.append(num)
            tempResult.append(temp)
        result.extend(tempResult)
        self.build(stack, result)

def test(args, expect):
    output = Solution().subsets(*args)
    print(f"{output == expect} case: {args}, output: {output}, expect: {expect} ")

test([[1,2,3]], [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]])
test([[0]], [[],[0]])

