# https://leetcode.com/problems/permutations/
from typing import List

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []
        self.dfs(nums, [], result)
        return result

    def dfs(self, nums: List[int], path: List[int], res: List[List[int]]) -> None:
        if not nums:
            res.append(path)
        for i in range(len(nums)):
            self.dfs(nums[:i] + nums[i+1:], path + [nums[i]], res)


def test(args, expect):
    output = Solution().permute(*args)
    print(f"{output == expect} case: {args}, output: {output}, expect: {expect}")

test([[1,2,3]], [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]])
test([[0, 1]], [[1]])

