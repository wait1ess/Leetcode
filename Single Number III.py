class Solution():                                  # 字典方法
    def singleNumber(self, nums):
        count ={}
        for element in nums:
            if element in count:count[element]+=1
            else: count[element]=1
        res = []
        for num, c in count.items():
            if c == 1:
                res.append(num)
        return res
