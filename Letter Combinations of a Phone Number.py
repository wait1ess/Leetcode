# 回溯法
class Solution:
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        phone = {'2': ['a', 'b', 'c'],
                 '3': ['d', 'e', 'f'],
                 '4': ['g', 'h', 'i'],
                 '5': ['j', 'k', 'l'],
                 '6': ['m', 'n', 'o'],
                 '7': ['p', 'q', 'r', 's'],
                 '8': ['t', 'u', 'v'],
                 '9': ['w', 'x', 'y', 'z']}
                
        def backtrack(combination, next_digits):
            if len(next_digits) == 0:                                             # 递归出口 如果没有下一个数字， 就将当前字符串combination加入结果列表
                output.append(combination)                                        
         
            else:                                                                 # 否则
                for letter in phone[next_digits[0]]:                              # 当前数字所代表的每一个字符
                    backtrack(combination + letter, next_digits[1:])              # 递归调用backtrack ，更新当前字符串连接字符为新的combination，取下一位数字
                    
        output = []
        if digits:
            backtrack("", digits)
        return output

if __name__=="__main__":
    digits="926"
    answer=Solution().letterCombinations(digits)
    print(answer)
