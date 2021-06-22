class Solution(object):
    buttons = {
        '2' : ['a', 'b', 'c'],
        '3' : ['d', 'e', 'f'],
        '4' : ['g', 'h', 'i'],
        '5' : ['j', 'k', 'l'],
        '6' : ['m', 'n', 'o'],
        '7' : ['p', 'q', 'r', 's'],
        '8' : ['t', 'u', 'v'],
        '9' : ['w', 'x', 'y', 'z']
    }

    def comb(self, l, acc):
        if len(l) == 0: return acc
        elif len(l) == 1: return self.buttons[l[0]]
        else:
            first_digit = l[0]
            digits = self.buttons[first_digit]
            result = []
            for d in digits:
                prev_comb = self.comb(l[1:], acc)
                for d_p in prev_comb:
                    result.append( d + d_p )
            return result
            
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        return self.comb(digits, [])

print(Solution().letterCombinations("2"))
