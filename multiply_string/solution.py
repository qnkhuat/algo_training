class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        #edge cases 
        if len(num1) == 0 or len(num2) == 0:
            return "0"
        result = [0] * len(num1 + num2)

        for i in reversed(range(len(num1))):
            n1 = num1[i]
            for j in reversed(range(len(num2))):
                n2 = num2[j]
                mul = result[i+j+1] + int(n1) * int(n2)
                result[i+j + 1] = mul % 10
                result[i+j] += mul // 10


        return "".join(map(str, result)).lstrip("0")


def test(args, expect):
    output = Solution().multiply(*args)
    print(f"{output == expect} case: {args}, output: {output}, expect: {expect} ")


test(["3", "2"], "6")
test(["15", "2"], "30")
test(["123", "456"], "56088")
test(["0", "0"], "0")


