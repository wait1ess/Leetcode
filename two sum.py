class Solution:
    def twoSum(self, nums, target):
        d={}
        for index,element in enumerate(nums):
            d[element]=[]
        for index,element in enumerate(nums):
            d[element].append(index)
        for a in nums :
            if  d.__contains__(target-a) and a!=target/2:
                return [d[a][0],d[target-a][0]]
            elif a==target/2 and len(d[a])>=2:
                return [d[a][0],d[a][1]]
if __name__ == "__main__":
    nums = [-1,-2,-3,-4,-5]
    target = -8
    answer=Solution().twoSum(nums,target)
    print(answer)


