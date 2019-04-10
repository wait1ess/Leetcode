class Solution:
    def fourSum(self, nums, target):
        d = dict()                            # 两数之和sum2为key 加数的索引组合（元祖）列表为value
        for i in range(len(nums)):            # 暴力列举
            for j in range(i+1,len(nums)):
                sum2 = nums[i]+nums[j]
                if sum2 in d:
                    d[sum2].append((i,j))
                else:
                    d[sum2] = [(i,j)]
        result = set()                        # 初始化结果集合
        for key in d:                         # 遍历所有sum2
            value = target - key              # 重新定目标值value
            if value in d:
                list1 = d[key]
                list2 = d[value]
                for (i,j) in list1:           # 已有的两数
                    for (k,l) in list2:       
                        if i!=k and i!=l and j!=k and j!=l:
                            flist = [nums[i],nums[j],nums[k],nums[l]]
                            flist.sort()      # 排序
                            result.add(tuple(flist))
        return list(result)

if __name__=="__main__":
    nums = [1, 0, -1, 0, -2, 2]
    target = 0
    answer=Solution().fourSum(nums, target)
    print(answer)
