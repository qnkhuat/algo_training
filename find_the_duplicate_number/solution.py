# https://leetcode.com/problems/find-the-duplicate-number/

class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        low = 1
        high = len(nums) - 1
        while low <= high:
            mid = (low + high) // 2
            count = 0

            count = sum([num <= mid for num in nums])
            if count > mid:
                duplicate = mid
                high = mid - 1
            else: 
                low = mid + 1

        return duplicate

def test(args, expect):
    output = Solution().exist(*args)
    print(f"{output == expect} case: {args}, output: {output}, expect: {expect} ")

