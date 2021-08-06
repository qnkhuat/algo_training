# https://leetcode.com/problems/longest-palindromic-substring/

class Solution(object):
    def longestPalindrome(self, s: str) -> str:

        longest = ""
        for i, c in enumerate(s):
            i_f = i
            i_b = i
            temp = ""
            while True:
                if i_f < 0 or i_b >= len(s): 
                    break
                if s[i_f] == s[i_b]:
                    temp = s[i_f:i_b+1]
                    if i_f > 1 and s[i_f - 1] == s[i_b] and len(temp)%2 == 1:
                        i_f -= 1
                    elif i_b < len(s) - 1 and s[i_f] == s[i_b+1] and len(temp) % 2 == 1:
                        i_b += 1
                    elif i_b > 1 and i_b < len(s) - 2 and len(temp) % 2 == 0:
                        i_f -= 1
                        i_b += 1
                    else: break
                else: break
            if len(temp) > len(longest):
                longest = temp
        return longest




def test(case, expect):
    output = Solution().longestPalindrome(case)
    print(f"{'Passed' if output == expect else 'Failed'} | case: {case}, output: {output}, expect: {expect} ")

test("babad", "aba")
test("cbbd", "bb")
test("a", "a")
test("ac", "a")
test("aacabdkacaa", "aca")
test("bb", "bb")
