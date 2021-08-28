from typing import List

class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        print(boxes)
        result = [0] * len(boxes)
        initialState = [0 if box == "0" else 1 for box in boxes]
        leftToRight = result.copy()
        rightToLeft = result.copy()
        
        lastStackLeft = initialState[0]
        lastStackRight = initialState[-1]
        for i in range(1, len(boxes)):
            leftToRight[i] = leftToRight[i-1] + lastStackLeft
            lastStackLeft += initialState[i]

            reversedI = len(boxes) - 1 - i
            rightToLeft[reversedI] = rightToLeft[reversedI+1] + lastStackRight
            lastStackRight+= initialState[reversedI]
        
        for i in range(len(boxes)):
            result[i] = leftToRight[i] + rightToLeft[i]
        return result


def test(args, expect):
    output = Solution().minOperations(*args)
    print(f"{output == expect} case: {args}, output: {output}, expect: {expect} ")


test(["001011"], [11, 8, 5, 4, 3, 4])
test(["110"], [1, 1, 3])
