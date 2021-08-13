# https://leetcode.com/problems/word-search/
from typing import List

#class Solution:
#    def exist(self, board: List[List[str]], word: str) -> bool:
#        wordMap = {}
#        m = len(board)
#        n = len(board[0])
#        for i in range(m):
#            for j in range(n):
#                char = board[i][j]
#                item = { 
#                        "used": False,
#                        "pos": (i, j)
#                        }
#                if char in wordMap.keys():
#                    wordMap[char].append(item)
#                else:
#                    wordMap[char] = [item]
#        
#
#        def isNear(a, b):
#            if (a[0] == b[0] and abs(a[1] - b[1]) == 1) or (a[1] == b[1] and abs(a[0] - b[0]) == 1):
#                return True
#            else: return False
#
#        def search(word, wordMap, currentPos):
#            if len(word) == 0: return True
#            char = word[0]
#            word = word[1:]
#            if char not in wordMap.keys() or unUsedCount = sum([True if item["used"] == False else False for item in wordMap[char] ]): 
#                return False
#
#            itemList = wordMap[char]
#            for item in itemList:
#                if item["used"]: continue
#                else: item["used"] = True
#
#                if currentPos == None or isNear(currentPos, item["pos"]):
#                    if search(word, wordMap, item["pos"]): return True
#                # reset
#                item["used"] = False
#
#            return False
#        return search(word, wordMap, None)

class Solution:
    def exist(self, board, word):
        if not board:
            return False

        for i in range(len(board)):
            for j in xrange(len(board[0])):
                if self.dfs(board, i, j, word):
                    return True
                return False

    # check whether can find word, start at (i,j) position
    def dfs(self, board, i, j, word):
        if len(word) == 0: # all the characters are checked
            return True
        if i<0 or i>=len(board) or j<0 or j>=len(board[0]) or word[0]!=board[i][j]:
            return False
        tmp = board[i][j]  # first character is found, check the remaining part
        board[i][j] = "#"  # avoid visit agian
        # check whether can find "word" along one direction
        res = self.dfs(board, i+1, j, word[1:]) or \
                self.dfs(board, i-1, j, word[1:]) or \
                self.dfs(board, i, j+1, word[1:]) or \
                self.dfs(board, i, j-1, word[1:])

        board[i][j] = tmp
        return res




def test(args, expect):
    output = Solution().exist(*args)
    print(f"{output == expect} case: {args}, output: {output}, expect: {expect} ")


test([[["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], "ABCCED"], True)
test([[["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], "SEE"], True)
test([[["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], "ABCB"], False)
test([[["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], "DEE"], True)
test([[["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], "SFF"], False)
test([[["a","b"],["c","d"]], "abcd"], False)
