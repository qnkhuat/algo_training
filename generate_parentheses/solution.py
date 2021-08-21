# link : https://leetcode.com/problems/generate-parentheses/

# Back tracking
# Choice: Place a "(" or ")"
# Constraints: Cannot until we open, Count of left open matters
# Goal: N*2 parentheses

class Solution:

    def generateParenthesis(self, n):
        if not n:
            return []
        left, right, ans = n, n, []
        self.dfs(left, right, ans, "")
        return ans

    def dfs(self, left, right, ans, string):
        if left > right:
            return

        if left == 0 and right == 0:
            ans.append(string)
            return

        if left > 0:
            self.dfs(left-1, right, ans, string + "(")

        if right > 0:
            self.dfs(left, right-1, ans, string + ")")


def test(case, result):
    output = Solution().generateParenthesis(case)
    print(f"case: {case}, {set(output) == set(result)}, output: {output}, expect: {result}")


test(1, ["()"])
test(2, ["()()","(())"])
test(3, ["((()))","(()())","(())()","()(())","()()()"])
