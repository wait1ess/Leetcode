# 摩尔投票算法( Boyer-Moore Voting Algorithm)
# 算法原理：每次从数组中找出一对不同的元素，将它们从数组中删除，直到遍历完整个数组。
#由于这道题已经说明一定存在一个出现次数超过一半的元素，所以遍历完数组后数组中一定会存在至少一个元素。
class Solution:
    def majorityElement(self, nums):
        count = 0
        candidate = None

        for num in nums:                     # 对于数组中每一个元素，
                                             # 首先判断count是否为0，
            if count == 0:             
                candidate = num              # 若为0，则把candidate设置为当前元素

                                             # 判断candidate是否与当前元素相等，若相等则count+=1，否则count-=1
            count += (1 if num == candidate else -1) 

        return candidate
