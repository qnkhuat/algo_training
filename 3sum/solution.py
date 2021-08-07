# https://leetcode.com/problems/3sum/
from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if len(nums) < 2:
            return []

        nums.sort()
        return self.searchSum(0, 3, nums)

    # nums must be a sorted array
    def searchSum(self, x: int, n:int, nums: List[int]) -> List[int]:
        if n == 1:
            for a in nums:
                if a == x:
                    return [[a]]
            return []
        else:
            output = []
            last = None
            for i, num in enumerate(nums):
                if num == last: continue # prevent duplicate candidates
                last = num

                candidates = self.searchSum((-num + x), n - 1, nums[i+1:])
                for cand in candidates:
                    cand.insert(0, num)
                    output.append(cand)
            return output

#class Solution:
#    def threeSum(self, nums: List[int]) -> List[List[int]]:
#        result = []
#        nums.sort()
#        for i, n in enumerate(nums):
#
#            if i > 0 and n == nums[i-1]:
#                continue
#
#            l, r = i + 1, len(nums) - 1
#            while l < r:
#                s = n + nums[l] + nums[r]
#                if s == 0:
#                    result.append([n, nums[l], nums[r]])
#                    while l < r and nums[l] == nums[l+1]:
#                        l += 1
#                    while l < r and nums[r] == nums[r-1]:
#                        r -= 1
#                    l += 1
#                    r -= 1
#                elif s < 0:
#                    l +=1
#                else: r -=1
#        return result

#Solution().threeSum([1, 2, -1, -1])
print(Solution().threeSum([-1,0,1,2,-1,-4]))
print(Solution().threeSum([0, 0, 0, 0]))
print(Solution().threeSum([-2,0,0,2,2]))
