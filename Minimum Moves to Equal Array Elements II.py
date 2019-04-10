class Solution:
    def minMoves2(self, nums):
        l=len(nums)
        if l<1 :return None
        if l==1: return 0
        def quick_sort(S,start,end):   # (子)数组的快速排序，start为在原数组上的开始索引
            if start>=end: return
            pivot=S[end]               # 轴
            left=start                 # 左游标
            right=end-1                # 右游标
            while left<=right:
                while left<=right and S[left]<=pivot: left+=1     
                while left<=right and S[right]>pivot: right-=1
                if left<=right:
                    S[left],S[right]=S[right],S[left]
                    left+=1
                    right-=1
            S[left],S[end]=S[end],S[left]      # 将轴放于“中间”，左小右大
            quick_sort(S,start,left-1)
            quick_sort(S,left+1,end)    
        quick_sort(nums,0,l-1)
        mid=l//2
        count=0
        for element in nums:
            count+=abs(nums[mid]-element)
        return count

if __name__=="__main__":
    nums=[1,2,3,4,5]
    answer=Solution().minMoves2(nums)
    print(answer)
