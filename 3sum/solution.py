# https://leetcode.com/problems/3sum/
from typing import List

#class Solution:
#    def threeSum(self, nums: List[int]) -> List[List[int]]:
#        if len(nums) < 2:
#            return []
#
#        nums.sort()
#        return self.findSum(0, 3, nums)
#
#    # nums must be a sorted array
#    def findSum(self, x: int, n:int, nums: List[int]) -> List[int]:
#        if n == 1:
#            for a in nums:
#                if a == x:
#                    return [[a]]
#            return []
#        else:
#            output = []
#            last = None
#            for i, num in enumerate(nums):
#                if num == last: continue # prevent duplicate candidates
#                last = num
#
#                candidates = self.findSum((-num + x), n - 1, nums[i+1:])
#                for cand in candidates:
#                    cand.insert(0, num)
#                    output.append(cand)
#            return output

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

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if len(nums) < 2:
            return []

        nums.sort()
        result = []
        self.findSum(0, 3, nums, [], result)
        return result

    # nums must be a sorted array
    def findSum(self, target: int, n:int, nums: List[int], cand: List[int], result: List[int]):
        if n == 2:
            l, r = 0, len(nums) - 1
            while l < r:
                twosum = nums[l] + nums[r]
                if twosum == target:
                    result.append(cand + [nums[l], nums[r]])

                    l+=1
                    # prevent duplication 
                    while l < r and nums[l] == nums[l - 1]:
                        l += 1

                elif twosum < target:
                    l+=1

                else:
                    r-=1
        else:
            for i, num in enumerate(nums[:len(nums) - n + 1]):
                if i == 0 or (i > 0 and nums[i-1] != num):
                    self.findSum(target - num, n - 1, nums[i+1:], cand + [num], result)

#Solution().threeSum([1, 2, -1, -1])
print(Solution().threeSum([-1,0,1,2,-1,-4]))
print(Solution().threeSum([0, 0, 0, 0]))
print(Solution().threeSum([-2,0,0,2,2]))
