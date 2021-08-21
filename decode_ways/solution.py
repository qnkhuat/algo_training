## https://leetcode.com/problems/decode-ways/
#class Solution:
#    # @param s, a string
#    # @return an integer
#    # 8:19
#    def numDecodings(self, s):
#        if s == '':
#            return 1
#
#        if s[0] == '0':
#            return 0
#
#        def isPossibleDouble(num):
#            return len(num) == 2 and (num[0] == '1' or (num[0] == '2' and num[1] <= '6'))
#
#        possibleDouble = True if isPossibleDouble(s[:2]) else False
#
#        if possibleDouble:
#            return self.numDecodings(s[1:]) + self.numDecodings(s[2:])
#        else:
#            return self.numDecodings(s[1:])

class Solution:
    def numDecodings(self, s: str) -> int:
        self.memo = {}

        def helper(s: str) -> int:
            if len(s) == 0: return 1
            if s in self.memo: return self.memo[s]

            takeOne = takeTwo = 0

            if int(s[:1]) >= 1 and int(s[:1]) <= 9:
                takeOne = helper(s[1:])

            if int(s[:2]) >= 10 and int(s[:2]) <= 26: 
                takeTwo = helper(s[2:])

            self.memo[s] = takeOne + takeTwo
            return self.memo[s]
        
        return helper(s)        

def test(args, expect):
    output = Solution().numDecodings(*args)
    print(f"{output == expect} case: {args}, output: {output}, expect: {expect} ")


test(["12"], 2)
test(["226"], 3)
test(["0"], 0)
test(["06"], 0)
test(["1"], 1)
test(["10"], 1)
test(["2101"], 1)
