class Solution:
    def diffWaysToCompute(self, input):
            """
            :type input: str
            :rtype: List[int]
            """
            def helper(m, n, op):
                if op == "+":
                    return m + n
                elif op == "-":
                    return m - n
                else:
                    return m * n
            if input.isdigit():
                return [int(input)]                 # 递归出口
            ans = []
            for i in range(len(input)):
                if input[i] in "+-*":               # 有运算符的地方
                    left = self.diffWaysToCompute(input[:i])          # 左部分递归
                    right = self.diffWaysToCompute(input[i + 1:])     # 右部分递归
                    print("left",left)
                    print("right",right)
                    ans.extend([helper(l, r, input[i]) for l in left for r in right])
                    print(input[i])
            return ans


if __name__=="__main__":
    inp="2*3-4*5"
    answer=Solution().diffWaysToCompute(inp)
    print(answer)
