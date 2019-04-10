class Solution():
    def threeSum(self, nums):
        res=[]
        nums.sort()    # 对原数组进行排序，然后开始遍历排序后的数组
        length = len(nums)
        for i in range(length-2): #[8] 遍历到到倒数第三个
            if nums[i]>0: break   #[7] 当遍历到正数的时候就break，三正数相加不可能为0
            if i>0 and nums[i]==nums[i-1]: continue #[1] 重复就跳过的处理，处理方法是从第二个数开始，如果和前面的数字相等，就跳过

            l, r = i+1, length-1 #[2]用两个指针分别指向fix数字之后开始的数组首尾两个数
            while l<r:
                total = nums[i]+nums[l]+nums[r] #和

                if total<0: #[3]小于target，则我们将左边那个指针i右移一位
                    l+=1
                elif total>0: #[4]大于target，则我们将右边那个指针j左移一位
                    r-=1
                else: #[5]等于target
                    res.append([nums[i], nums[l], nums[r]])
                    while l<r and nums[l]==nums[l+1]: #[6]避免重复答案
                        l+=1
                    while l<r and nums[r]==nums[r-1]: #[6]避免重复答案
                        r-=1
                    l+=1
                    r-=1
        return res
if __name__=="__main__" :
    nums =[-4,-2,-2,-2,0,1,2,2,2,3,3,4,4,6,6]
    answer=Solution().threeSum(nums)
    print(answer)
        
