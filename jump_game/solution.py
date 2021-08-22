from typing import List
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        m = 0
        for i, n in enumerate(nums):
            if m < i:
                return False
            m = max(m, i + n)
        return True 

    #def canJump(self, nums: List[int]) -> bool:
    #    def walk(nums: List[int]):
    #        if len(nums) == 1: return True

    #        n = nums[0] if nums[0] <= len(nums) - 1 else len(nums) - 1
    #        for i in range(n, 0, -1):
    #            if walk(nums[i:]):
    #                return True

    #        return False
    #        
    #    return walk(nums)


def test(args, expect):
    output = Solution().canJump(*args)
    print(f"{output == expect} case: {args}, output: {output}, expect: {expect} ")


test([[2,3,1,1,4]], True)
test([[3,2,1,0,4]], False)
test([[5,4,3,2,1]], True)
test([[5,4,3,2,1,0,0]], False)
test([[0]], True)
test([[1]], True)



