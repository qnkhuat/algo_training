from typing import List

class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        minN = float('inf')
        maxN = 0
        sumN = 0
        for n in nums:
            if n < 1: continue
            sumN += n

            if n <= minN:
                minN = n
            if n >= maxN:
                maxN = n

        if minN > 1: return 1
        
        if continuousSum == sumN: return maxN + 1
        else: return continuousSum - sumN

            
    
def test(args, expect):
    output = Solution().firstMissingPositive(*args)
    print(f"{output == expect} case: {args}, output: {output}, expect: {expect} ")

test([[1, 2, 0]], 3)
test([[3, 4, -1, 1]], 2)
test([[3, 4, -1, 1, 1]], 2)
test([[7,8,9,11,12]], 1)



