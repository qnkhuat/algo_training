# link : https://leetcode.com/problems/combination-sum/

# Given an array of distinct integers candidates and a target integer target, return a list of all unique combinations of candidates where the chosen numbers sum to target. You may return the combinations in any order.
# The same number may be chosen from candidates an unlimited number of times. Two combinations are unique if the frequency of at least one of the chosen numbers is different.
# It is guaranteed that the number of unique combinations that sum up to target is less than 150 combinations for the given input.


# Choice: one number in candidates
# Constraints: 
# Goal: sum(comb) = target

class Solution(object):
    def dfs(self, candidates, target, result, comb=[]):
        if target == 0: 
            result.append(comb)
            return
        comb_sum = sum(comb)
        last_cand = comb[-1] if len(comb) > 0 else 0
        for cand in candidates:
            if target - cand >= 0 and cand >= last_cand:
                temp_comb = comb.copy()
                temp_comb.append(cand)
                self.dfs(candidates, target - cand, result, temp_comb)
    
    def combinationSum(self, candidates, target):
        result = []
        self.dfs(candidates, target, result)
        return result


def test(args, expect):
    output = Solution().combinationSum(*args)
    print(f"{output == expect} case: {args}, output: {output}, expect: {expect} ")

test([[2, 3, 5], 8], [[2,2,2,2],[2,3,3],[3,5]])
test([[2], 1], [])
test([[1], 1], [[1]])
